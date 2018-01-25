from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, DecimalValidator

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
 

class Location(models.Model):
    # -90.00000 < latitude < 90.000
    latitude  = models.DecimalField(max_digits=8,decimal_places=6,
                    validators=[MaxValueValidator(90),MinValueValidator(-90),
                                DecimalValidator(7,5),])
    # -180.00000 < longitude < 180.00000
    longitude = models.DecimalField(max_digits=9,decimal_places=6,
                    validators=[MaxValueValidator(180),MinValueValidator(-180),
                                DecimalValidator(8,5),])

# a CalendarSlot has a starting point and a duration, and can be recurring
class CalendarSlot(models.Model):
    
    start_time = models.TimeField(verbose_name='from')
    end_time = models.TimeField(verbose_name='to',null=True)
    start_date = models.DateField(verbose_name='starting')
    repeat = models.BooleanField(verbose_name='repeat',default=False)
    repeat_every = models.IntegerField(verbose_name='every') #,min_value=1,max_value=999)
    REPEATFREQS = ['days','weeks']
    # repeat_freq = models.ChoiceField(choices=tuple([(y,y) for y in REPEATFREQS]))
    repeat_freq = models.CharField(default='weeks',max_length=200,
                                choices=tuple([(y,y) for y in REPEATFREQS]))

    REPEATDAYS = [('Monday','M'),
                  ('Tuesday','T'),
                  ('Wednesday','W'),
                  ('Thursday','T'),
                  ('Friday','F'),
                  ('Saturday','S'),
                  ('Sunday','S'),
                  ]
    repeat_days = models.CharField(choices=REPEATDAYS,max_length=200,)

    end_type = models.CharField(max_length=200,
                                choices=tuple([(y,y) for y in ['never','on','after']]))
    end_date = models.DateField(verbose_name='ending',blank=True,null=True)
    n_recurrences = models.IntegerField(verbose_name='recurrences')
    
    # many calendar slots can be associated with an event request
    event_request = models.ForeignKey('EventRequest',related_name='calendar_slots',
                                        on_delete=models.CASCADE)
    
    # one calendar slot is associated with an event
    event = models.OneToOneField('Event',related_name='calendar_slot',
                                        on_delete=models.CASCADE)
    
    # one calendar slot is associated with a venue slot
    venue = models.OneToOneField('Venue',related_name='calendar_slot',
                                        on_delete=models.CASCADE)


class Venue(models.Model):
    # Example of a venue: "UNSW Gym Yoga room 2, capacity 25 people, available
    # for rent by the general public Mon and Wed afternoons 2-5pm for $30ph"
    name = models.CharField(max_length=200,default='')

    location = models.OneToOneField(Location,on_delete=models.CASCADE,null=True)
    
    capacity = models.PositiveIntegerField(default=0)

    cost_per_hour = models.DecimalField(max_digits=7,decimal_places=5,
                        validators=[MinValueValidator(0),DecimalValidator(7,5)])
                        
    def __str__(self):
        return self.name
 

# define static variables used by the Event and EventRequest classes
EVENT_TYPES = ['Yoga','Rockclimbing','Tango','Freediving']
TRAVEL_TYPES = ['Rideshare','Walk','Cycle','Public Transport','Drive']
                
                
class Event(models.Model):
    # Example of an event: "Yoga class with Mary (charging $45) in UNSW gym yoga
    # room 2 (charging $20), for up to 20 people, on Fri Jan 12th 3pm for one hour
    
    
    # Manually set a few different types of events for now.
    event_type = models.CharField('type of event',default='Yoga',max_length=200,
                                choices=tuple([(y,y) for y in EVENT_TYPES]))

    # Events have a many-to-many relationship with Attendees. A person can attend
    # many events, and an event can have many people attending.
    attendees = models.ManyToManyField(Person,related_name='events_attending')
    
    # Events have a many-to-one relationship with Organizers. An organizer can
    # host many events, but an event can only have one organizer. 'related_name' is
    # needed because Event also links to Person via the attendees field
    organizer = models.ForeignKey(Person,related_name='events_organizing',
                                    on_delete=models.CASCADE,null=True)
    organizer_fee = models.DecimalField(default=0,max_digits=6,decimal_places=0,
                        validators=[MinValueValidator(0),DecimalValidator(6,0)])

    # Events have a many-to-one relationship with Venues. A venue can host many
    # events, but an event can only have one venue.
    venue = models.ForeignKey(Venue,related_name='events_hosting',
                                on_delete=models.CASCADE,null=True)
    venue_fee = models.DecimalField(default=0,max_digits=6,decimal_places=0,
                        validators=[MinValueValidator(0),DecimalValidator(6,0)])

    # capacity
    min_people = models.PositiveIntegerField(default=1)
    max_people = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.event_type
 

class EventRequest(models.Model):
    # Example of an event request: "I want to attend yoga class any weekday 5-8pm
    # at a cost (including travel cost) of no more than $8"
    
    # each event request is created by a person
    person_requesting = models.ForeignKey('Person',related_name='events_requested',
                                            on_delete=models.CASCADE,null=True)
    
    # event types are manually defined, there are only a few of them
    # yoga, rockclimbing, tango, freediving
    event_type = models.CharField('type of event',default='Yoga',blank=False,max_length=200,
                                choices=tuple([(y,y) for y in EVENT_TYPES]))

    # maximum cost (including travel cost) of the class
    max_cost = models.DecimalField('maximum cost of the event (including travelling)',
                    default=0,max_digits=6,decimal_places=0,
                    validators=[MinValueValidator(0),DecimalValidator(6,0)])
                
    # travel options
    travel_types = models.CharField('travel options',default='Rideshare',max_length=200,
                                choices=tuple([(y,y) for y in TRAVEL_TYPES]))
    
    # cost of time, per minute
    travel_time_cost = models.DecimalField('cost of time spent travelling (in mins)',
                                default=0,max_digits=5,decimal_places=2,
                                validators=[MinValueValidator(0),DecimalValidator(5,2)])
                    
                
    def __str__(self):
        return self.event_type
 
