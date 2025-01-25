from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Room(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     members = models.ManyToManyField(User, related_name='rooms_joined', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_rooms')

#     def __str__(self):
#         return f"{self.title}, (Created by {self.created_by})"
    

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sent_messages', null=True)
    content = models.TextField()
    #room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.sender}: {self.content[:50]}..." 