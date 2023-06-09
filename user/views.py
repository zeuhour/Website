from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse, HttpRequest
# Create your views here.
def createuser(request: HttpRequest):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        birthday = data['birthday']
        phonenumber = data['phonenumber']
        email = data['email']
        passwd = make_password(password=data["password"], hasher='pbkdf2_sha256')