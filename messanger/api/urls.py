from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [

]

router = routers.SimpleRouter()
router.register(r'message', MessageViewSet, basename='message')
router.register(r'room', RoomViewSet, basename='room')

urlpatterns += router.urls

