from django.shortcuts import render
from django.http import HttpResponse
from scripter.utilities import text_speech

def index(request):
    return render(request,'scripter/scripter.html')
# Create your views here.

def submitdata(request):
    if request.method == 'POST':
        print(request.POST)
        #To insert into the database

        #To pass the same data to Google API
        # text_speech([("Can I come in?", "male"), ("Yes, sure", "female")])

        #To process the results and store it in the database



        return HttpResponse("Loading the web page")
    elif request.method == 'GET':
        return HttpResponse("Loading the web page")
