from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registerPage', views.registerPage),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('profile/<int:id>', views.profilePage),
    path('profile/create/story', views.new_story),
    path('create/story', views.new_story),
    path('story/edit/<int:id>', views.edit),
    path('story/update/<int:id>', views.update),
    path('story/delete/<int:id>', views.destroy),
    path('story/<int:id>', views.read_one_story),
    path('profile/edit/<int:id>', views.edit_profile),
    path('profile/update/<int:id>', views.update_profile)
]