from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    birthday = models.DateField()
    createtime = models.DateTimeField(auto_now_add=True)
    phonenumber = models.CharField(max_length=20, unique=True, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    deltag = models.BooleanField(default=False)