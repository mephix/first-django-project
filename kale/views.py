from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # ... do any python stuff ...
    
    # all Django wants finally is this HttpResponse
    return HttpResponse('welcome to Kal, an app for scheduling classes and events')

def whatclass(request):
    eventchoices = Event.category.choices
    
    return HttpResponse(eventchoices)
    
#    return HttpResponse('What class do you want to take?')
    
def when(request):
    return HttpResponse('What days and times are you free?')
    
def howmuch(request):
    return HttpResponse('Whats the maximum you are willing to pay for a class?')
    
def travel(request):
    return HttpResponse('travel preferences coming soon')
    
def okcool(request):
    return HttpResponse('ok cool, we will find a class for you')