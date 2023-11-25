from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from item.models import item
from .models import conversation
from .forms import conversationmessageform




# Create your views here.
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404 (item,pk= item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    conversations = conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)
    if request.method =='POST':
        form = conversationmessageform(request.POST)
        if form.is_valid():
            conversation= conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('item:detail', pk=item_pk)
    else:
        form = conversationmessageform()
    return render(request,'conversation/new.html',{
        'form': form
    })
@login_required
def inbox(request):
    conversations = conversation.objects.filter(members__in=[request.user.id])
    return render (request, 'conversation/inbox.html',{
        'conversations': conversations
    })
@login_required
def detail(request, pk):
    conversation = conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = conversationmessageform(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = conversationmessageform()

    return render (request, 'conversation/detil.html', {
        'conversation': conversation,
        'form': form

    })
    


