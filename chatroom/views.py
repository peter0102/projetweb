from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from django.contrib import messages
# Create your views here.

@login_required(login_url='login') # l'utilisateur ne peut accéder à home s'il n'est pas connecté
def home(request):
    if request.method=='POST':
        roomNameWanted=request.POST['room-Name']
        if Room.objects.filter(roomName=roomNameWanted).exists() :
            messages.error(request,"That chatroom already exists, please choose another name")
        else :
            newRoom=Room(roomName=roomNameWanted)
            newRoom.save()
            return redirect('/chatroom/room_name='+roomNameWanted+'/')
    allRooms=Room.objects.all()
    return render(request,'chatroom/home.html',{'allRooms': allRooms})

@login_required(login_url='login') # l'utilisateur ne peut accéder à home s'il n'est pas connecté
def rooms(request,roomName):
    if request.method=='POST':
        messageSent=request.POST['messageSent']
        newMessage=Message(message=messageSent)
        newMessage.save()
    allMessages=Message.objects.all()
    nameOfTheRoom=roomName
    username=request.user.get_username()
    return render(request,'chatroom/room.html',{ 'nameOfTheRoom' : nameOfTheRoom, 'username':username})