from os import name
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

    # Comment CRUD Commands
    path('post/comment/<int:id>', views.post_comment),
    path('delete/comment/<int:id>/story/<int:story_id>', views.destroy_comment),

    # Favorite and Unfavorite stories
    path('favorite/<int:id>', views.favorite_story),
    path('unfavorite/<int:id>', views.unfavorite_story),
    path('favorite/stories/<int:id>', views.users_favorite_stories),

    # filter stories
    path('filter/stories/<genre>', views.filter_stories),
    path('filter/stories/<genre>/<genre_two>', views.filter_stories_two),
]