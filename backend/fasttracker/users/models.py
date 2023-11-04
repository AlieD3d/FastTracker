from django.db import models


class Users(models.Model):
    username = models.CharField(verbose_name='Имя пользователя', max_length=54)
    email = models.EmailField(verbose_name='Email', unique=True, max_length=254)
    avatar = models.ImageField(upload_to='images/')