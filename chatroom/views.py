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
            return redirect('/chatroom/room_name='+roomNameWanted+'/') #crée des url personnalisées en fonction du nom du salon
    allRooms=Room.objects.all()
    return render(request,'chatroom/home.html',{'allRooms': allRooms})

@login_required(login_url='login') # l'utilisateur ne peut accéder à home s'il n'est pas connecté
def rooms(request,roomName):
    nameOfTheRoom=roomName
    username=request.user.get_username()
    chatRoomName=Room.objects.get(roomName=nameOfTheRoom)
    return render(request,'chatroom/room.html',{ 'nameOfTheRoom' : nameOfTheRoom, 'username':username, 'chatRoomName':chatRoomName})

def sendMessage(request):
    if request.method=='POST':
        messageSent=request.POST['messageSent']
        chatRoomName=request.POST['chatRoomName']
        user=request.user.get_username()
        newMessage=Message(message=messageSent,where=chatRoomName,who=user) #on sauvegarde le message
        newMessage.save()
        return JsonResponse({'success': True})

def getMessage(request,roomName):
    nameOfTheRoom=roomName
    chatRoomName=Room.objects.get(roomName=nameOfTheRoom)
    allMessagesList=Message.objects.filter(where=chatRoomName) #on ne récupère que les messages du salon souhaité
    allMessagesJson=[{'allMessagesValue':message.message, 'who':message.who} for message in allMessagesList] #on récupère la valeur allMessageValue message.message(champ de la classe Message), un seul message aurait donné la classe, le deuxième donne la ième valeur
    return JsonResponse({"allMessagesList":allMessagesJson})
