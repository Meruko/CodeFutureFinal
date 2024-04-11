from .models import *
from django.contrib.auth.models import User

INVITE_CODE_LENGTH = 20


def get_user_rooms(user: User):
    rooms = Room.objects.filter(members__in=[user])
    return rooms


def get_room_messages(room: Room):
    messages = Message.objects.filter(room=room, is_deleted=False).order_by('datetime')
    return messages


def generate_invite_code():
    invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=INVITE_CODE_LENGTH))

    while Room.objects.filter(invite_code=invite_code).exists():
        invite_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=INVITE_CODE_LENGTH))

    return invite_code
