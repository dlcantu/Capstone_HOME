from django.shortcuts import render, redirect
from .models import Client, Goals

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
    clients = Client.objects.all().order_by('lastName')
    print(clients)
    context = {
        'clients': clients
    }
    return render(request, 'client.html', context)

def dashboard(request):
    dashboard_deadlines = Goals.objects.all().order_by('goalEndDate').filter(goals=False)
    print(dashboard_deadlines)
    context = {
        'dashboard_deadlines': dashboard_deadlines
    }
    return render(request, 'home.html', context)

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
        query_name = request.POST.get('lastName', None)
        if query_name:
            client_info = Client.objects.filter(lastName__contains=query_name)
            current_client = Client.objects.get(lastName=query_name)
            client_goal = Goals.objects.filter(selectClient=current_client).filter(goals=False) #list of all goals
            print(client_goal)
            return render(request, "clientsearch.html", {"client_info":client_info, "client_goal":client_goal})
    return render(request, "clientsearch.html")

def goal_status(request, id):
    if request.method == "POST":
        goal_choice = bool(request.POST['goals'])
        goal_status = Goals.objects.get(id=id)
        goal_status.goals = goal_choice #access Boolean and make it not what it already is. Flips it to oppostie
        goal_status.save()
        return render(request, "clientsearch.html")
    if (request.POST['goals'] == 'True'):
        goal_choice= Goals.objects.filter(dateCreated=goal_choice).delete()
    else:
        goal_status.goals = False
        goal_status.save()
        return redirect('clientsearch.html')
    return render(request, "clientsearch.html")
