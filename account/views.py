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
        if form.is_valid(): 
            form.save() #si les données remplies sont correctes, on les sauvegarde et cela crée l'utilisateur
            messages.success(request,"Compte crée, veuillez vous connecter")
            return redirect('login') #redirection vers la page login
        else:
            messages.error(request,"Erreur lors de la création du compte, veuillez recommencer")
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
