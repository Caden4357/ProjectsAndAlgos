from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registerPage', views.registerPage),
    path('register', views.register),
    path('login', views.login),
    path('success', views.registered),
    path('logout', views.logout)
]