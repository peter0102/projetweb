from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .myforms import UserForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout,get_user_model
from django.contrib.auth.models import Group
from django.contrib import messages
# Create your views here.
def register(request):
    form=UserForm()
    if request.user.is_authenticated: #si l'utilisateur est connecté, il ne doit pas pouvoir accéder aux pages register et login
        return redirect('home') #home defini dans chatroom\urls.py
    if request.method=='POST' :
        password1=request.POST['password1']
        password2=request.POST['password2']
        username=request.POST['username']
        User=get_user_model()
        if not User.objects.filter(username=username).exists():
            if not password1 == "":
                if password1 == password2 :
                    User.objects.create_user(username=username,password=password1)
                    newGroup = Group.objects.get_or_create(name ='isNotMuted') #on crée un groupe pour les utilisateurs muets
                    getGroup=Group.objects.get(name='isNotMuted') #on récupère le groupe
                    user=User.objects.get(username=username) #on récupère l'utilisateur
                    user.groups.add(getGroup) #on ajoute l'utilisateur au groupe
                    allGroups=Group.objects.all()
                    for group in allGroups:
                        user.groups.add(group) #on ajoute l'utilisateur à tous les groupes pour qu'il puisse accéder à tous les salons
                    messages.success(request,"Account created, you can sign in")
                    return redirect('login') #redirection vers la page login
                else:
                    messages.error(request,"Those passwords didn't match, please try again")
            else:
                messages.error(request,"The password field is empty")
        elif User.objects.filter(username=username).exists():
            messages.error(request,"This username is already taken")
        else:
            messages.error(request,"Error, the password isn't strong enough")
    context={'form':form}
    template=loader.get_template('account/register.html')
    return HttpResponse(template.render(context,request))

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request,"Signed in")
            return redirect('home')
        else:
            messages.error(request,"Wrong password or username")
            return redirect('login')
    return render(request,'account/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')
