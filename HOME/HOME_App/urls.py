from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('homepage/', views.home, name = 'homepage'),
    path('deadlines/', views.deadlines, name = 'deadlines'),
    path('newclient/', views.newclient, name = 'newclient')
]