from django.contrib import admin

# Register your models here.
from .models import conversation, conversationmessage

admin.site.register(conversation)
admin.site.register(conversationmessage)