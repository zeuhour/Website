from django.urls import path

from user import views

urlpatterns = [
    path('create', views.createUser),
    path('login', views.Login),
    path('adduser', views.add_user),
    path('logout', views.Logout),
    path('delete', views.deleteUser),
    path('changepw', views.changepassword),
    path('test', views.test)
]