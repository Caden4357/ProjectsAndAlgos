from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registerPage', views.registerPage),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('create/story', views.new_story)
]