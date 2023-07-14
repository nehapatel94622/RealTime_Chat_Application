from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=10000)

class Message(models.Model):
    value = models.CharField(max_length=1000000000)
    date = models.DateTimeField(auto_now_add=True, auto_created=True)
    user = models.CharField(max_length=20000000000)
    room = models.CharField(max_length=200000000)


