from django.db import models
from django.contrib.auth.models import User
from item.models import item
# Create your models here.
class conversation(models.Model):
    item= models.ForeignKey(item , related_name='conversations' , on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversaions')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField (auto_now=True)

    class meta:
        ordering = ('-modified_at',)
class conversationmessage(models.Model):
    conversation = models.ForeignKey(conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete= models.CASCADE)
    


