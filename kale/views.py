from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import TYPE_CHOICES, EventRequest

def index(request):
    user = {'hasevents': False, 'hasvenues': False}
    context = {'user': user}
    return render(request,'kale/index.html',context)

def findclass(request):
    context = {'type_choices': TYPE_CHOICES}
    # render takes a request object, a template and an optional dictionary
    return render(request,'kale/findclass.html',context)

# server method to handle the posted data
def findclass_post(request):
    try:
        selected_category = request.POST['choice']
    except (KeyError):
        return render(request,'kale/findclass.html', {
            'type_choices': TYPE_CHOICES,
            'error_message': "You didn't select a class.",
        })
    else:
        # create a new EventRequest
        e = EventRequest(category=selected_category)

        # so far we only know the category, not the max_cost or associated
        # CalendarSlots. we should know the Person but we havent captured
        # that yet
        e.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('kale:when',args=(e.id,)))
        
        
def when(request, event_request_id):
    event_request = get_object_or_404(EventRequest,pk=event_request_id)
    days_of_the_week = ['mon','tue','wed','thu','fri','sat','sun']
    context = { 'event_request': event_request,
                'days_of_the_week': days_of_the_week,
    }
    return render(request,'kale/when.html',context)
    
def when_post(request, event_request_id):
    try:
        selected_day = request.POST['day']
    except (KeyError):
        return render(request,'kale/when.html', {
            'type_choices': TYPE_CHOICES,
            'error_message': "You didn't select days",
        })
    else:
        e = get_object_or_404(EventRequest,pk=event_request_id)
        # give the EventRequest associated CalendarSlots
        # !!! DONT KNOW HOW TO DO THIS YET !!!

        e.save()

        # continue on to next page
        return HttpResponseRedirect(reverse('kale:howmuch',args=(e.id,)))
        
        
def howmuch(request, event_request_id):
    event_request = get_object_or_404(EventRequest,pk=event_request_id)
    context = {'event_request': event_request}
    return render(request,'kale/howmuch.html',context)

def howmuch_post(request, event_request_id):
    try:
        max_cost = request.POST['max_cost']
    except (KeyError):
        return render(request, 'kale/howmuch.html', {
            'type_choices': TYPE_CHOICES,
            'error_message': "You didn't select the maximum you are willing to pay",
        })
    else:
        e = get_object_or_404(EventRequest,pk=event_request_id)
        e.max_cost = max_cost
        e.save()

        # continue on to next page
        return HttpResponseRedirect(reverse('kale:travel',args=(e.id,)))
        
        
def travel(request, event_request_id):
    event_request = get_object_or_404(EventRequest,pk=event_request_id)
    context = {'event_request': event_request}
    return render(request,'kale/travel.html',context)


def travel_post(request, event_request_id):
    try:
        travel_cost = request.POST['travel_cost']
    except (KeyError):
        return render(request,'kale/travel.html', {
            'type_choices': TYPE_CHOICES,
            'error_message': "You didn't select your cost of travel time",
        })
    else:
        e = get_object_or_404(EventRequest,pk=event_request_id)
        e.travel_cost = travel_cost
        e.save()

        # continue on to next page
        return HttpResponseRedirect(reverse('kale:okcool',args=(e.id,)))
        

def okcool(request, event_request_id):
    event_request = get_object_or_404(EventRequest,pk=event_request_id)
    context = {'event_request': event_request}
    return render(request,'kale/okcool.html'    ,context)

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
