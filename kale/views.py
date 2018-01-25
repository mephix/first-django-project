from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import EventRequest, EVENT_TYPES, TRAVEL_TYPES
from .forms import CalendarSlotForm, EventRequestForm, EventForm, VenueForm, LocationForm

def index(request):
    user = {'hasevents': False, 'hasvenues': False}
    context = {'user': user}
    return render(request,'kale/index.html',context)
    
def newclass(request):
    eventRequestFields = ('event_type','max_cost','travel_types','travel_time_cost')
    calendarSlotFields = ('start_time','end_time','start_date','repeat','repeat_every',
                        'repeat_freq','repeat_days','end_type','end_date','n_recurrences')
    # if method is POST, we need to process the form data that is being posted
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        eventRequestData = {k: request.POST[k] for k in eventRequestFields}
        calendarSlotData = {k: request.POST[k] for k in calendarSlotFields}
        eventRequestForm = EventRequestForm(eventRequestData)
        # check whether it is valid
        if eventRequestForm.is_valid():
            # process the data in cleaned_data as required
            e = EventRequest(**eventRequestForm.cleaned_data)
            e.save()
            
        # create the associated CalendarSlot
        calendarSlotForm = CalendarSlotForm(calendarSlotData)
        if calendarSlotForm.is_valid():
            c = CalendarSlot(event_request=e,**calendarSlotForm.cleaned_data)
            c.save()

        # redirect to a new URL
        return HttpResponseRedirect('kale/index.html')

    # if a GET (or any other) method, create blank forms
    else:
        eventRequestForm = EventRequestForm()
        calendarSlotForm = CalendarSlotForm()
        
    # if GET method or the form was not valid, it will be blank now
    return render(request, 'kale/newclass.html', {'eventRequestForm': eventRequestForm,
                                                  'calendarSlotForm': calendarSlotForm,}
    )
    

def kalendar(request):
    context = {}
    return render(request,'kale/kalendar.html',context)

def myevents(request):
    context = {}
    return render(request,'kale/myevents.html',context)

def newevent(request):
    eventFields = ('event_type','organizer_fee','min_people','max_people')
    calendarSlotFields = ('start_time','end_time','start_date','repeat','repeat_every',
                          'repeat_freq','repeat_days','end_type','end_date','n_recurrences')
    # if method is POST, we need to process the form data that is being posted
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        eventData = {k: request.POST[k] for k in eventFields}
        calendarSlotData = {k: request.POST[k] for k in calendarSlotFields}
        eventForm = EventForm(eventData)
        # check whether it is valid
        if eventForm.is_valid():
            # process the data in form.cleaned_data as required
            e = Event(**eventForm.cleaned_data)
            e.save()
            
        # create the associated CalendarSlot
        calendarSlotForm = CalendarSlotForm(calendarSlotData)
        if calendarSlotForm.is_valid():
            c = CalendarSlot(event=e,**calendarSlotForm.cleaned_data)
            c.save()

        # redirect to a new URL
        return HttpResponseRedirect('kale/index.html')

    # if a GET (or any other) method, create blank forms
    else:
        eventForm = EventForm()
        calendarSlotForm = CalendarSlotForm()
        
    # if GET method or the form was not valid, it will be blank now
    return render(request, 'kale/newevent.html', {'eventForm': eventForm,
                                                  'calendarSlotForm': calendarSlotForm,}
    )

def myvenues(request):
    context = {}
    return render(request,'kale/myvenues.html',context)

def newvenue(request):
    venueFields = ('name','location','capacity','cost_per_hour')
    locationFields = ('latitude','longitude')

    # if method is POST, we need to process the form data that is being posted
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        venueData = {k: request.POST[k] for k in venueFields}
        locationData = {k: request.POST[k] for k in locationFields}
        venueForm = VenueForm(venueData)
        locationForm = LocationForm(locationData)

        # create the Location
        locationForm = LocationForm(locationData)
        if locationForm.is_valid():
            l = Location(**locationForm.cleaned_data)
            l.save()

        # create the Venue
        if venueForm.is_valid():
            # process the data in form.cleaned_data as required
            v = Venue(location=l,**venueForm.cleaned_data)
            v.save()
            
        # redirect to a new URL
        return HttpResponseRedirect('kale/index.html')

    # if a GET (or any other) method, create blank forms
    else:
        venueForm = VenueForm()
        locationForm = LocationForm()
        
    # if GET method or the form was not valid, it will be blank now
    return render(request, 'kale/newvenue.html', {'venueForm': venueForm,
                                                  'locationForm': locationForm,}
    )
