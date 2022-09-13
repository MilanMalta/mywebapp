from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    
    result = requests.get('https://kuzelka.sk')
    return HttpResponse(result)
    
    
    


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
