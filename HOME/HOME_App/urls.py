from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('homepage/', views.dashboard, name = 'homepage'),
    path('deadlines/', views.deadlines, name = 'deadlines'),
    path('client/', views.clientlist, name = 'client'),
    path('newclient/', views.add_newclient, name = 'newclient'),
    path('clientsearch/', views.client_search, name = 'clientsearch'),
    path('goalstatus/<int:id>', views.goal_status, name = 'goalstatus')
]