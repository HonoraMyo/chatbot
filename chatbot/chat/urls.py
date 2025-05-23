from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room>/', views.room, name= 'room'),
    path('checkview', views.checkview, name= 'ckeckview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name= 'getMessages'),
]