from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('chatroom/home/',views.home,name='home'),
    path('chatroom/room_name=<str:roomName>/',views.rooms,name='room'), #pour obtenir une url personnalisée en fonction du nom du salon
    path('send/<str:roomName>/',views.sendMessage,name='send'),
    path('get/<str:roomName>/',views.getMessage,name='get')

]