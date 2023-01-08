from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from django.contrib import messages
from django.http import JsonResponse
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
    nameOfTheRoom=roomName
    username=request.user.get_username()
    roomId=Room.objects.get(roomName=nameOfTheRoom)
    return render(request,'chatroom/room.html',{ 'nameOfTheRoom' : nameOfTheRoom, 'username':username, 'roomId':roomId})

def sendMessage(request):
    if request.method=='POST':
        messageSent=request.POST['messageSent']
        roomId=request.POST['roomId']
        user=request.user.get_username()
        newMessage=Message(message=messageSent,where=roomId,who=user) #on récupère le salon où a été envoyé le message
        newMessage.save()
        return JsonResponse({'success': True})

def getMessage(request,roomName):
    nameOfTheRoom=roomName
    roomId=Room.objects.get(roomName=nameOfTheRoom)
    allMessagesList=Message.objects.filter(where=roomId.id) #on ne récupère que les messages du salon souhaité
    allMessagesJson=[{'allMessagesValue':message.message, 'who':message.who} for message in allMessagesList] #on récupère la valeur allMessageValue message.message(champ de la classe Message), un seul message aurait donné la classe, le deuxième donne la ième valeur
    return JsonResponse({"allMessagesList":allMessagesJson})
