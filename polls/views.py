from . import main
import openai
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from bs4 import BeautifulSoup
import requests
from glob import glob
import os,nltk,aiml
import pytholog as pl
from py2neo import Graph
base_path = os.path.join(os.getcwd()+'/polls/backend/')
openai.api_key = os.getenv('SECRET_KEY')

graph = Graph("bolt://localhost:7687" , auth=("neo4j","12345678"))

# import nltk
#from nltk import pos_tag
#nltk.download('averaged_perceptron_tagger')


def Home(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request, 'index.html')

#AIML files
myBot = aiml.Kernel()
for files in glob('files/*.aiml'):
    myBot.learn(files)

#Pytholog queries
kb = pl.KnowledgeBase("parent")

def generate_response(request,message):
    for word,digit in nltk.pos_tag(nltk.word_tokenize(message)):
        if "VB" in digit:
            if word == "solve":
                exp = message[5:]
                return eval(exp)
        if "NN" in digit:
            if word == "calculate":
                exp = message[9:]
                return eval(exp)
    
    myBot.setBotPredicate("master", "Asad")
    resp = myBot.respond(message)
    Father = myBot.getPredicate("father")
    print(Father)
    UserName = request.user
    print(UserName)
    if Father:
        kb([f"isFatherof({Father},{UserName})"])
        fathId = graph.evaluate("create (p:Person {name:$name}) return id(p)",name=Father)
        print(fathId)
        userId = graph.evaluate(f"match (u:User) where u.username = '{UserName}' return id(u)")
        print(userId)
        graph.run(f"match (u:User),(p:Person) where id(u) = {userId} and id(p) = {fathId} "
        " create (p)-[:isFatherof]->(u)")
    token = nltk.pos_tag(nltk.word_tokenize(resp))
    Father = None
    for word,digit in token:
        if "WRB" in digit or "DT" in digit:
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message,
            max_tokens=200
            )
            return response.choices[0].text.strip()
            
    if "unknown" in resp:
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message,
            max_tokens=200
            )
            return response.choices[0].text.strip()
    else:
        return resp


def bot_response(request):
    message = request.POST.get('message')
    return HttpResponse(
        generate_response(request,message)
    )

'''graph.run("""
MERGE(n:Owner {{name: $fullname , email:$email , password:$password}}),
{name = fullname, email = email, password = password}
""")
'''