# Generated by Django 4.2 on 2024-06-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
