from django.contrib import admin

# Register your models here.
from .models import Category, item
admin.site.register(Category)
admin.site.register(item)