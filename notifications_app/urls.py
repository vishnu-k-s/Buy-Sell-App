
#chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.chatroom, name='chatroom'),
   
]