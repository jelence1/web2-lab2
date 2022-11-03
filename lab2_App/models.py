from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    role = models.CharField(max_length=1000)

class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    nickname = models.CharField(max_length=1000)
