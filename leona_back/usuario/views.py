from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class ValidarTokenView(APIView):
    def post(self, request):
        token_data = request.data.get('token')
        token = Token.objects.filter(key=token_data).first()

        if token:
            user = token.user
             
            return Response({'user': user.username}, status=200)

        return Response({'valido': False}, status=400)

class AuthView(APIView):
    def post(self, request):
        user_data = request.data.get('username')
        password_data = request.data.get('password')

        user = authenticate(username=user_data, password=password_data)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': user.username,
                'token': token.key,
                'password': user.password
            }, status=200)

        return Response({'error': 'Usuario o contraseña incorrectos'}, status=400)
