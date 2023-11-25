from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from item.models import item

@login_required
def index(request):
    items = item.objects.filter(created_by=request.user)
    return render (request, 'dashboard/index.html', {'items':items,})
