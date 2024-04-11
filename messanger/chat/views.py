from django.shortcuts import render, redirect, get_object_or_404
from .utils import *
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.decorators.http import require_POST

from chat.forms import *
from chat.models import Room, Message

# Create your views here.
@login_required
def index(request):
    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            room_name = form.cleaned_data['name']
            room = Room.objects.create(name=room_name, invite_code=generate_invite_code())
            room.members.add(request.user)
            return redirect('room', pk=room.pk)
    else:
        form = RoomForm()
        form_invite = RoomInviteForm()
    context = {
        'form': form,
        'form_invite': form_invite
    }
    return render(request, 'chat/index.html', context=context)

@login_required()
def user_rooms(request):
    rooms = get_user_rooms(request.user)
    context = {
        'rooms': rooms
    }
    return render(request, 'chat/room.html', context=context)

@login_required
def get_room(request, pk):
    room = get_object_or_404(Room, id=pk)
    if request.method == "POST":
        text = request.POST['text']
        message = Message(sender=request.user, text=text)
        message.save()
        room.messages.add(message)
        print(f'{message=}')
        return redirect('room', pk=room.pk)

    rooms = get_user_rooms(request.user)
    messages = get_room_messages(room)

    print(f'{messages=}')
    context = {
        'room': room,
        'rooms': rooms,
        'room_messages': messages,
        'form': MessageForm()
    }
    return render(request, 'chat/room.html', context=context)

@login_required
@require_POST
def get_room_by_invite(request):
    form = RoomInviteForm(request.POST)
    invite = request.POST['invite_code']
    room = get_object_or_404(Room, invite_code=invite)
    messages = get_room_messages(room)
    rooms = get_user_rooms(request.user)

    if not room.members.contains(request.user):
        room.members.add(request.user)

    context = {
        'room': room,
        'rooms': rooms,
        'room_messages': messages,
        'form': MessageForm()
    }
    return render(request, 'chat/room.html', context=context)

@login_required()
def leave_room(request, pk):
    room = get_object_or_404(Room, id=pk)
    room.members.remove(request.user)

    if room.members.count() <= 0:
        room.delete()

    return redirect('index')
