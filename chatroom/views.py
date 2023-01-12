from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
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

#à partir d'ici, que des vues qui gèrent les requêtes ajax

def sendMessage(request):
    if request.method=='POST':
        messageSent=request.POST['messageSent']
        chatRoomName=request.POST['chatRoomName']
        if messageSent=="":
            return JsonResponse({'isEmpty': True})
        user=request.user.get_username()
        newMessage=Message(message=messageSent,where=chatRoomName,who=user) #on sauvegarde le message
        newMessage.save()
        return JsonResponse({'isEmpty': False})

def getMessage(request,roomName): #paramètre roomName nécessaire pour ne récupérer que les messages d'un salon
    allMessagesList=Message.objects.filter(where=roomName) #on ne récupère que les messages du salon souhaité
    allMessagesJson=[{'allMessagesValue':message.message, 'who':message.who, 'messageId':message.id} for message in allMessagesList] #on récupère la valeur allMessageValue message.message(champ de la classe Message), un seul message aurait donné la classe, le deuxième donne la ième valeur
    #on récupère aussi l'id du message pour ensuite simplifier la suppression de message
    return JsonResponse({"allMessagesList":allMessagesJson})

def messageDelete(request):
    if request.method=='POST':
        messageId=request.POST['messageId']
        message=Message.objects.get(id=messageId)
        message.delete()
        return JsonResponse({'success': True})
def getRooms(request):
    allRooms=Room.objects.all()
    allRoomsJson=[{'roomName':room.roomName} for room in allRooms]
    return JsonResponse({"allRooms":allRoomsJson})
def roomDelete(request):
    if request.method=='POST':
        roomName=request.POST['roomName']
        room=Room.objects.get(roomName=roomName)
        room.delete()
        allMessagesList=Message.objects.filter(where=roomName)
        for message in allMessagesList: #on supprime tous les messages du salon, au cas où si on recrée un salon portant le même nom que le salon supprimé
            message.delete()
        return JsonResponse({'success': True})
def admin(request):
    if request.user.is_superuser:
        return render(request,'chatroom/admin.html')
    else:
        return redirect('home')
def getUsers(request):
    User=get_user_model() #pour récupérer le modèle User, et ensuite récupérer ses objets
    users=User.objects.all()
    usersJson=[{'username':user.username} for user in users]
    return JsonResponse({"users":usersJson})
def setSuperUser(request):
    if request.method=='POST':
        username=request.POST['username']
        User=get_user_model()
        user=User.objects.get(username=username)
        if user.is_superuser :
            return JsonResponse({'isSuperUser': True})
        user.is_superuser=True
        user.save()
        return JsonResponse({'isSuperUser': False})
def unsetSuperUser(request):
    if request.method=='POST':
        username=request.POST['username']
        User=get_user_model()
        user=User.objects.get(username=username)
        if not user.is_superuser :
            return JsonResponse({'isNotSuperUser': True})
        user.is_superuser=False
        user.save()
        return JsonResponse({'isNotSuperUser': False})
def deleteUser(request):
    if request.method=='POST':
        username=request.POST['username']
        User=get_user_model()
        user=User.objects.get(username=username)
        user.delete()
        return JsonResponse({'success': True})