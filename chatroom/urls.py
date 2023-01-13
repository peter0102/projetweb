from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('chatroom/home/',views.home,name='home'),
    path('chatroom/room_name=<str:roomName>/',views.rooms,name='room'), #pour obtenir une url personnalisée en fonction du nom du salon
    path('chatroom/admin/',views.admin,name='admin'),
    path('send/',views.sendMessage,name='send'),
    path('get/<str:roomName>/',views.getMessage,name='get'), #on passe le nom du salon en paramètre dans la vue associée, pour ne récupérer ensuite que les messages d'un salon
    path('getRooms/',views.getRooms,name='getRooms'),
    path('deleteMessage/',views.messageDelete,name="messageDelete"),
    path('deleteRoom/',views.roomDelete,name="roomDelete"),
    path('getUsers/',views.getUsers,name='users'),
    path('setSuperUser/',views.setSuperUser,name='setSuperUser'),
    path('unsetSuperUser/',views.unsetSuperUser,name='unsetSuperUser'),
    path('deleteUser/',views.deleteUser,name='deleteUser'),
    path('muteUser/',views.muteUser,name='muteUser'),
    path('unmuteUser/',views.unmuteUser,name='unmuteUser'),
]