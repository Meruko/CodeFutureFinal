from django.urls import path
from . import views

urlpatterns = [
    # path('', views.news, name='news'),
    path('', views.NewsList.as_view(), name='news'),
    path('news_form', views.NewsCreate.as_view(), name='news_form'),
    path('<int:id>', views.NewsDetail.as_view(), name='one_news'),
    path('<int:pk>/update', views.NewsUpdate.as_view(), name='one_news_update'),
    path('<int:pk>/delete', views.NewsDelete.as_view(), name='one_news_delete'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
    path('search/', views.search_results, name='search_results'),

    path('contact/', views.contact_email, name='email_page'),

    path('api/test/', views.test_json, name='api_test'),
    path('api/news/', views.news_api_list, name='api_news_list'),
    path('api/news/<int:pk>/', views.news_api_detail, name='api_news_detail')
]

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/news_vs', views.NewsViewSet, basename='news')

urlpatterns += router.urls