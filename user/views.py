from django.shortcuts import render
from user.models import UserInfo
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpRequest
from tools.logger import logger_request
from tools.resp import JsonResponse_zh
from django.contrib.auth.models import User

# Create your views here.
@logger_request('user')
def createUser(request: HttpRequest):
    if request.method == 'POST' and request.POST:
        data = request.POST

        if not UserInfo.objects.filter(phonenumber = data['phonenumber']).exists():            
            try:
                UserInfo.objects.create(
                    name = data['name'], 
                    birthday = data['birthday'], 
                    phonenumber = data['phonenumber'],
                    )
                return JsonResponse_zh({"msg" : "创建成功！"})
            except Exception as e:
                return JsonResponse_zh({"msg" : str(e)})
        elif UserInfo.objects.filter(phonenumber = data['phonenumber']).values()[0]['deltag'] == True:
            try:
                UserInfo.objects.filter(phonenumber = data['phonenumber']).update(
                    name = data['name'], 
                    birthday = data['birthday'],
                    deltag = False
                    )
                return JsonResponse_zh({"msg" : "创建成功！"})
            except Exception as e:
                return JsonResponse_zh({"msg" : str(e)})
        else:
            return JsonResponse({"msg" : "该手机号码已经注册！"}, json_dumps_params={'ensure_ascii':False})
    
@logger_request('user')
def deleteUser(request: HttpRequest):
    User.objects.filter(username = request.user).update(is_active=0) 

@logger_request('user')
def add_user(request: HttpRequest):
    if request.method == 'POST' and request.POST:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username = username).values()[0]
        if user:
            if user['is_active'] == 1:
                return JsonResponse_zh({'msg': '用户已存在！'})
            else:
                User.objects.filter(username=username).update(is_active=1)
                u = User.objects.get(username=username)
                u.set_password(password)
                u.save()
                return JsonResponse_zh({'msg':'创建成功！'})
        else:
            User.objects.create_user(username = username, password = password)
            return JsonResponse_zh({'msg': '创建成功！'})

@logger_request('user')
def Login(request: HttpRequest):
    if request.method == 'POST' and request.POST:
        data = request.POST
        if User.objects.filter(username = data["username"]).exists():
            #自带用户验证方法，验证通过返回User对象
            u = authenticate(request=request, username = data['username'], password = data['password'])
            if u:
                if u.is_active:
                    #自带登录方法
                    login(request=request, user=u)
                    return JsonResponse_zh({"msg" : "登录成功！"})
                else:
                    return JsonResponse_zh({"msg" : "用户未激活！"})
            else:
                return JsonResponse_zh({"msg" : "用户名或密码错误！"})
        else:
            return JsonResponse_zh({"msg" : "用户不存在！"})
        
@logger_request('user')
def Logout(request: HttpRequest):
    logout(request)
    return JsonResponse_zh({"msg" : "登录已注销！"})

@logger_request('user')
def changepassword(request: HttpRequest):
    u = User.objects.get(username=request.user)
    u.set_password(request.POST['password'])
    u.save()
    return JsonResponse_zh({'msg':'修改完成！'})

@logger_request('test')
def test(request: HttpRequest):
    # return render(request, 'index.html')
    return JsonResponse_zh({'msg':'完成'})