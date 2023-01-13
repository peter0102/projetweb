from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2'] # on ne garde que les champs username, paswword1 le mot de passe, et password2 la confirmation