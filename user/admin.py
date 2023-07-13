from django.contrib import admin

#Register your models here.
from . import models

admin.site.register(models.UserInfo) #添加希望在admin后台管理的模型