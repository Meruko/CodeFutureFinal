from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.user_registration, name='regis'),
    path('login/', views.user_login, name='log in'),
    path('logout/', views.user_logout, name='log out')
]