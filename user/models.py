from django.db import models
from django.utils import timezone
#from django.contrib.auth.hashers import make_password, check_password
#from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=10)
    birthday = models.DateField()
    phonenumber = models.CharField(max_length=20, unique=True, primary_key=True)
    deltag = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     self.password = make_password(password=self.password, hasher="pbkdf2_sha1")
    #     super(User, self).save(*args, **kwargs)