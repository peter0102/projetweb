from django.db import models

# Create your models here.
class Room(models.Model):
    roomName=models.CharField(max_length=50)
    def __str__(self):
        return self.roomName

class Message(models.Model):
    message=models.CharField(max_length=10000)
    where=models.CharField(max_length=1000) #dans quel salon a été envoyé le message
    who=models.CharField(max_length=1000) #qui a envoyé le message.
    when=models.CharField(max_length=1000) #quand a été envoyé le message
    def __str__(self):
        return self.message