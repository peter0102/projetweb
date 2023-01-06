from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .myforms import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
# Create your views here.
def register(request):
    if request.user.is_authenticated: #si l'utilisateur est connecté, il ne doit pas pouvoir accéder aux pages register et login
        return redirect('home')
    form=User()
    if request.method=='POST' :
        form=User(request.POST)
        password1=request.POST['password1']
        password2=request.POST['password2']
        if form.is_valid(): 
            form.save() #si les données remplies sont correctes, on les sauvegarde et cela crée l'utilisateur
            messages.success(request,"Compte crée, veuillez vous connecter")
            return redirect('login') #redirection vers la page login
        if password1 != password2 :
            messages.error(request,"Erreur lors de la création du compte, les mots de passe de correspondent pas")
        else:
            messages.error(request,"Erreur lors de la création du compte, l'identifiant existe déjà ou le mot de passe n'est pas assez compliqué ou mot de passe trop proche de l'identifiant")
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
            messages.success(request,"Connecté")
            return redirect('home')
        else:
            messages.error(request,"Nom d'utilisateur ou mot de passe incorrect")
            return redirect('login')
    return render(request,'account/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')
