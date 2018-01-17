from django.shortcuts import render
from django.http import Http404
from .models import TYPE_CHOICES

def index(request):
    user = {'hasevents': False, 'hasvenues': False}
    context = {'user': user}
    return render(request,'kale/index.html',context)

def findclass(request):
    context = {'type_choices': TYPE_CHOICES}
    # render takes a request object, a template and an optional dictionary
    return render(request,'kale/findclass.html',context)
    
def when(request):
    context = {}
    return render(request,'kale/findclass/when.html',context)
    
def howmuch(request):
    context = {}
    return render(request,'kale/findclass/howmuch.html',context)
    
def travel(request):
    context = {}
    return render(request,'kale/findclass/travel.html',context)

def okcool(request):
    context = {}
    return render(request,'kale/findclass/okcool.html',context)

def kalendar(request):
    context = {}
    return render(request,'kale/kalendar.html',context)

def myevents(request):
    context = {}
    return render(request,'kale/myevents.html',context)

def newevent(request):
    context = {}
    return render(request,'kale/newevent.html',context)

def myvenues(request):
    context = {}
    return render(request,'kale/myvenues.html',context)

def newvenue(request):
    context = {}
    return render(request,'kale/newvenue.html',context)
