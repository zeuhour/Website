from django.urls import path

from . import views

urlpatterns = [
    path('WOAcover/', views.WOAcover)
]