from django.urls import path
from . import views

urlpatterns = [
    # login and registration 
    path('', views.index),
    path('registerPage', views.registerPage),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

    # Users dashboard and profile CRUD commands 
    path('dashboard', views.dashboard),
    path('profile/<int:id>', views.profilePage),
    path('profile/create/story', views.new_story),
    path('profile/edit/<int:id>', views.edit_profile),
    path('profile/update/<int:id>', views.update_profile),

    # story CRUD commands
    path('create/story', views.new_story),
    path('story/edit/<int:id>', views.edit),
    path('story/update/<int:id>', views.update),
    path('story/delete/<int:id>', views.destroy),
    path('story/<int:id>', views.read_one_story),
]