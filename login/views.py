from django.shortcuts import render
from py2neo import Graph
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

graph = Graph("bolt://localhost:7687" , auth=("neo4j","12345678"))
# graph.run("create (b:Talkitron {name:$name})",name="Talkitron")

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/chat")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect("/login")

def register_page(request):
    if request.method == "POST":
        first = request.POST['first']
        last = request.POST['last']
        username = request.POST['username']
        email= request.POST["email"]
        password = request.POST['pass']
        user = User.objects.create_user(
            first_name=first,
            last_name=last,
            username=username,
            email=email,
            password=password
        )
        datatoget={ "fname": first,"lname": last,"username": username,"email": email,"password": password}
        graph.run("create (n:Person:User {fname:$fname,lname:$lname,username:$username,password:$password,email:$email})",**datatoget)
        graph.run("match (n),(b) where n.username = $username and id(b) = 0 "
        "merge (b)-[:KNOWS]->(n)",username=username)
        user.save()
        login(request, user)
        return redirect("/chat")
    return render(request, 'register.html')
