
# chat/views.py
from django.shortcuts import render

def chat(request):
    return render(request, 'chat/chat.html')


def chatroom(request, room_name):
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name
    })

'''
def room(request):
    return render(request, 'chat/room.html', {
        'room_name': "user"
    })
'''