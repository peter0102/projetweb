from django.db import models

# Create your models here.
class Room(models.Model):
    roomName=models.CharField(max_length=50)
    def __str__(self):
        return self.roomName