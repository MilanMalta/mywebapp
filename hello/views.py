from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    
    response = requests.get('http://cas.sk')
    return HttpResponse(response) 
    
    
    


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
