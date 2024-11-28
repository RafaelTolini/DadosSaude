from django.urls import path

from base.views.message_view import delete_message, update_message, activities
from .views.home_view import home
from .views.room_view import room, create_room, update_room, delete_room
from .views.auth_view import login_view, logout_view, register_view
from .views.user_view import user_profile, update_user
from .views.topic_view import topics_view
from .views.drc_view import drc_view
from .views.neo_view import neo_view
from .views.dac_view import dac_view
from .views.dm_view import dm_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user_profile/<int:id>/', user_profile, name='user_profile'),
    path('room/<str:pk>/', room, name='room'),
    path('create_room/', create_room, name='create_room'),
    path('update_room/<int:id>/', update_room, name='update_room'),
    path('delete_room/<int:id>/', delete_room, name='delete_room'),
    path('delete_message/<int:id>/', delete_message, name='delete_message'),
    path('update_message/<int:id>/', update_message, name='update_message'),
    path('update_user/<int:id>/', update_user, name='update_user'),
    path('topics/', topics_view, name='topics'),
    path('activities/', activities, name='activities'),
    
    path('drc/', drc_view, name='drc'),
    path('neo/', neo_view, name='neo'),
    path('dac/', dac_view, name='dac'),
    path('dm/', dm_view, name='dm'),
]
