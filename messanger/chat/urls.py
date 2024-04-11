from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('room/<int:pk>', views.RoomDetailView.as_view(), name='room'),
    path('room/<int:pk>', views.get_room, name='room'),
    path('room/by_invite', views.get_room_by_invite, name='room_by_invite'),
    path('room/by_user', views.user_rooms, name='user_rooms'),
    path('room/<int:pk>/leave', views.leave_room, name='leave_room')
]