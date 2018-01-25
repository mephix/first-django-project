from django.forms import ModelForm, SelectDateWidget, CheckboxSelectMultiple
from django.forms import RadioSelect, SelectMultiple, TimeInput, DateInput
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, DecimalValidator
import datetime
from .models import Location, Venue, CalendarSlot, EventRequest, Event

class CalendarSlotForm(ModelForm):
    class Meta:
        model = CalendarSlot
        fields = ['start_time','end_time','start_date','repeat','repeat_every',
                  'repeat_freq','repeat_days','end_type','end_date','n_recurrences']
        widgets = { 'start_time': TimeInput,
                    'end_time': TimeInput,
                    'start_date': DateInput,
                    'end_date': SelectDateWidget,
                    'repeat_freq': RadioSelect(attrs={'required':False}),
                    'repeat_days': CheckboxSelectMultiple(attrs={'required':False}),
                    'end_type': RadioSelect,}
    

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_type','organizer_fee','min_people','max_people']

    
class EventRequestForm(ModelForm):
    class Meta:
        model = EventRequest
        fields = ['event_type','max_cost','travel_types','travel_time_cost']
        widgets = {'travel_types': CheckboxSelectMultiple}
    
    
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name','location','capacity','cost_per_hour']
        # widgets = {'travel_types': CheckboxSelectMultiple}
    

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['latitude','longitude']

    
    
"""
    # type of event
    event_type = forms.ChoiceField(label='What class do you want to take?',
                                    choices=tuple([(y,y) for y in EVENT_TYPES]))
    
    # maximum cost of the event
    max_cost = forms.DecimalField(label='Whats the maximum youre willing to pay for the class?',
                                min_value=0,max_digits=6,decimal_places=0,)
                                # validators=[MinValueValidator(0),DecimalValidator(6,0)],)
                            
    # use all these fields to create CalendarSlots
    start_time = forms.TimeField(label='from',
                    initial=datetime.datetime.now())
    end_time = forms.TimeField(label='to',
                    initial=(datetime.datetime.now()+datetime.timedelta(hours=1)))
    start_date = forms.DateField(label='starting',
                    initial=datetime.datetime.today())
    repeat = forms.BooleanField(label='repeat',initial=True)
    repeat_every = forms.IntegerField(label='every',initial=1,min_value=1,max_value=999)
    repeat_unit = forms.ChoiceField(choices=tuple([(y,y) for y in ['days','weeks']]),
                                    initial='days')
    DAYSOFTHEWEEK = [('Monday','M'),
                     ('Tuesday','T'),
                     ('Wednesday','W'),
                     ('Thursday','T'),
                     ('Friday','F'),
                     ('Saturday','S'),
                     ('Sunday','S'),
                     ]
    repeat_days = forms.MultipleChoiceField(choices=DAYSOFTHEWEEK,)
    end_type = forms.ChoiceField(choices=tuple([(y,y) for y in ['never','on','after']]),
                                initial='never',widget=forms.RadioSelect)
    end_date = forms.DateField(label='ending',
                    initial=(datetime.datetime.today()+datetime.timedelta(weeks=1)))
    recurrences = forms.IntegerField(label='recurrences',initial=5,min_value=1,max_value=999)
    
    # types of travel
    travel_types = forms.ChoiceField(label='How are you willing to get there?')

    # cost of travel
    travel_time_cost = forms.DecimalField(label='The cost to me of every minute spent travelling is:',
                            min_value=0,max_digits=4,decimal_places=1,)
                            #validators=[MinValueValidator(0),DecimalValidator(5,2)],)
    
    # !!! associated Person !!!
    # have to get this from login
    
"""