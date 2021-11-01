from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)

class UserToken(models.Model):
    user = models.OneToOneField('User',on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
