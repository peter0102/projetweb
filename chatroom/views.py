from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import Group,User
from django.utils import timezone, dateformat
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
            newGroup = Group.objects.get_or_create(name =roomNameWanted)
            getGroup=Group.objects.get(name=roomNameWanted)
            allUsers=User.objects.all() #on ajoute tous les utilisateurs au groupe pour qu'ils puissent accéder au salon, pour bloquer l'accès à certains utilisateurs
            for user in allUsers:
                user.groups.add(getGroup)
            return redirect('/chatroom/room_name='+roomNameWanted+'/') #crée des url personnalisées en fonction du nom du salon
    allRooms=Room.objects.all()
    return render(request,'chatroom/home.html',{'allRooms': allRooms})

@login_required(login_url='login') # l'utilisateur ne peut accéder à rooms s'il n'est pas connecté
def rooms(request,roomName):
    nameOfTheRoom=roomName
    username=request.user.get_username()
    user = User.objects.get(username=request.user.get_username()) #on récupère l'utilisateur pas en string mais en objet
    chatRoomName=Room.objects.get(roomName=nameOfTheRoom) #on récupère le nom du salon pour savoir dans quel salon le message a été envoyé
    if user.groups.filter(name=chatRoomName).exists() :
        return render(request,'chatroom/room.html',{ 'nameOfTheRoom' : nameOfTheRoom, 'username':username, 'chatRoomName':chatRoomName})
    else :
        messages.error(request,"You can't enter this chatroom")
        return redirect('/chatroom/home/')

#à partir d'ici, que des vues qui gèrent les requêtes ajax

def sendMessage(request):
    date = dateformat.format(timezone.now(), 'd-m-Y H:i') #on formate la date pour l'afficher correctement
    if request.method=='POST':
        messageSent=request.POST['messageSent']
        chatRoomName=request.POST['chatRoomName']
        user = User.objects.get(username=request.user.get_username())
        getGroup=Group.objects.get(name='isNotMuted') #on récupère le groupe
        canEnter=Group.objects.get(name=chatRoomName)
        if user.groups.filter(name=canEnter).exists() : #on vérifie que l'utilisateur est bien dans le groupe du salon
            if user.groups.filter(name=getGroup).exists() : #si l'utilisateur est dans le groupe isNotMuted, il peut envoyer des messages
                if Room.objects.filter(roomName=chatRoomName).exists() :
                    if messageSent=="":
                        return JsonResponse({'isEmpty': True})
                    newMessage=Message(message=messageSent,where=chatRoomName,who=user,when=date) #on sauvegarde le message
                    newMessage.save()
                    return JsonResponse({'isEmpty': False})
                else :
                    return JsonResponse({'roomExists': True})
            else :
                return JsonResponse({'isMuted': True}) #si l'utilisateur n'est pas dans le groupe isNotMuted, il ne peut pas envoyer de message
        else :
            return JsonResponse({'canEnter': True})

def getMessage(request,roomName): #paramètre roomName nécessaire pour ne récupérer que les messages d'un salon
    allMessagesList=Message.objects.filter(where=roomName) #on ne récupère que les messages du salon souhaité
    allMessagesJson=[{'allMessagesValue':message.message, 'who':message.who, 'messageId':message.id,'when':message.when} for message in allMessagesList] #on récupère la valeur allMessageValue message.message(champ de la classe Message), un seul message aurait donné la classe, le deuxième donne la ième valeur
    #on récupère aussi l'id du message pour ensuite simplifier la suppression de message
    return JsonResponse({"allMessagesList":allMessagesJson})
#à partir d'ici, que des vues qui gèrent les requêtes ajax pour l'admin
def messageDelete(request):
    if request.user.is_superuser: #on vérifie que l'utilisateur est bien un admin, au cas où un utilisateur perd ses droits d'admin mais qu'il a encore la page ouverte
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
    if request.user.is_superuser: 
        if request.method=='POST':
            roomName=request.POST['roomName']
            room=Room.objects.get(roomName=roomName)
            room.delete()
            allMessagesList=Message.objects.filter(where=roomName)
            for message in allMessagesList: #on supprime tous les messages du salon, au cas où si on recrée un salon portant le même nom que le salon supprimé
                message.delete()
            getGroup=Group.objects.get(name=roomName)
            getGroup.delete()
            return JsonResponse({'success': True})
def admin(request):
    if request.user.is_superuser:
        return render(request,'chatroom/admin.html')
    else:
        return redirect('home')
def getUsers(request):
    if request.user.is_superuser:
        User=get_user_model() #pour récupérer le modèle User, et ensuite récupérer ses objets
        users=User.objects.all()
        usersJson=[{'username':user.username} for user in users]
        return JsonResponse({"users":usersJson})
def setSuperUser(request):
    if request.user.is_superuser:
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
    if request.user.is_superuser:
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
    if request.user.is_superuser:
        if request.method=='POST':
            username=request.POST['username']
            User=get_user_model()
            user=User.objects.get(username=username)
            user.delete()
            return JsonResponse({'success': True})
def muteUser(request):
    if request.user.is_superuser:
        if request.method=='POST':
            username=request.POST['username']
            User=get_user_model()
            user=User.objects.get(username=username)
            getGroup=Group.objects.get(name='isNotMuted')
            if not user.groups.filter(name=getGroup).exists() :
                return JsonResponse({'isMuted': True})
            user.groups.remove(getGroup)
            return JsonResponse({'isMuted': False})
def unmuteUser(request):
    if request.user.is_superuser:
        if request.method=='POST':
            username=request.POST['username']
            User=get_user_model()
            user=User.objects.get(username=username)
            getGroup=Group.objects.get(name='isNotMuted')
            if user.groups.filter(name=getGroup).exists() :
                return JsonResponse({'isNotMuted': True})
            user.groups.add(getGroup)
            return JsonResponse({'isNotMuted': False})
def banUser(request): #ne permet que de bannir un utilisateur du salon dans lequel l'admin qui effectue l'action se trouve
    if request.user.is_superuser:
        if request.method=='POST':
            username=request.POST['username']
            roomName=request.POST['roomName']
            User=get_user_model()
            user=User.objects.get(username=username)
            getGroup=Group.objects.get(name=roomName)
            if not user.groups.filter(name=getGroup).exists() :
                return JsonResponse({'isBanned': True})
            user.groups.remove(getGroup)
            return JsonResponse({'isBanned': False})
def unbanUser(request): #ne permet que de débannir un utilisateur du salon dans lequel l'admin qui effectue l'action se trouve
    if request.user.is_superuser:
        if request.method=='POST':
            username=request.POST['username']
            roomName=request.POST['roomName']
            User=get_user_model()
            user=User.objects.get(username=username)
            getGroup=Group.objects.get(name=roomName)
            if user.groups.filter(name=getGroup).exists() :
                return JsonResponse({'isNotBanned': True})
            user.groups.add(getGroup)
            return JsonResponse({'isNotBanned': False})
