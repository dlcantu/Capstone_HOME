from django.shortcuts import render, redirect
from .models import Client, Goals

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/login.html')

def deadlines(request):
    if request.method=="POST":
        client_id = request.POST['clients']
        dateCreated = request.POST['createddate']
        goalEndDate = request.POST['endofgoal']
        goalNotes = request.POST['goalnotes']
        current_client = Client.objects.get(id=client_id)
        Goals.objects.create(selectClient = current_client, dateCreated = dateCreated, goalEndDate = goalEndDate, goalNotes = goalNotes)
        print(client_id)
        return redirect('deadlines')
    else:
        clients = Client.objects.all()
        return render(request, 'deadlines.html', {"clients": clients})

def clientlist(request):
    clients = Client.objects.all()
    print(clients)
    context = {
        'clients': clients
    }
    return render(request, 'client.html', context)

def add_newclient(request):
    if request.method=="POST":
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        dateOfBirth = request.POST['dob']
        clientNotes = request.POST['clientnotes']
        Client.objects.create(firstName = firstName, lastName = lastName, dateOfBirth = dateOfBirth, clientNotes = clientNotes)
        return redirect('client') #redirect to name
    else:
        return render(request, 'newclient.html') #render html

def client_search(request):
    if request.method == "POST":
        query_name = request.POST.get('firstName', None)
        if query_name:
            client_info = Client.objects.filter(firstName__contains=query_name)
            current_client = Client.objects.get(firstName=query_name)
            client_goal = Goals.objects.filter(selectClient=current_client)
            return render(request, "clientsearch.html", {"client_info":client_info, "client_goal":client_goal})
    return render(request, "clientsearch.html")

    