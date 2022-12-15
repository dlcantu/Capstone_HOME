from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/login.html')

def deadlines(request):
    return render(request, 'deadlines.html')

def newclient(request):
    return render(request, 'newclient.html')

