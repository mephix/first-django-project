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

# a CalendarSlot has a starting point and a duration
# CalendarSlots cannot be recurring: multiple slots will have to be created to
# represent a recurring slot
class CalendarSlot(models.Model):
    startDateTime = models.DateTimeField()
    duration = models.DurationField()

    # many calendar slots can be associated with an event request
    event_request_slots = models.ForeignKey('EventRequest',related_name='event_request',
                                        on_delete=models.CASCADE)
    
    # one calendar slot is associated with an event
    event_slots = models.OneToOneField('Event',related_name='event',
                                        on_delete=models.CASCADE)
    
    # one calendar slot is associated with a venue slot
    venue_slots = models.OneToOneField('VenueSlot',related_name='venue_slot',
                                        on_delete=models.CASCADE)
    

# a VenueSlot is a CalendarSlot plus a price
class VenueSlot(models.Model):
    # price is expressed per hour. Note that the calendar_slot can be any amount
    # of time. So if price_per_hour is 30, and the slot is for 3 hours, then if
    # this whole slot gets booked, its cost needs to be calculated as 30*3 = 90,
    # not simply taken as 30
    price_per_hour = models.DecimalField(max_digits=7,decimal_places=5,
                        validators=[MinValueValidator(0),DecimalValidator(7,5)])
                        
    # many VenueSlots are associated with a Venue
    venue = models.ForeignKey('Venue',related_name='venue',
                                on_delete=models.CASCADE)

    
class Venue(models.Model):
    # Example of a venue: "UNSW Gym Yoga room 2, capacity 25 people, available
    # for rent by the general public Mon and Wed afternoons 2-5pm for $30ph"
    name = models.CharField(max_length=200,default='')

    location = models.OneToOneField(Location,on_delete=models.CASCADE,null=True)
    
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
 
    # see VenueSlots for availability
    
  
# define this static variable used by the Event and EventRequest classes
TYPE_CHOICES = (('Yoga','Yoga'),
                ('Rockclimbing','Rockclimbing'),
                ('Tango','Tango'),
                ('Freediving','Freediving'))
                
                
class Event(models.Model):
    # Example of an event: "Yoga class with Mary (charging $45) in UNSW gym yoga
    # room 2 (charging $20), for up to 20 people, on Fri Jan 12th 3pm for one hour
    
    # Manually set a few different types of events for now.
    category = models.CharField('type of event',choices=TYPE_CHOICES,default='Yoga',
                                max_length=200)

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
        return self.category
 

class EventRequest(models.Model):
    # Example of an event request: "I want to attend yoga class any weekday 5-8pm
    # at a cost (including travel cost) of no more than $8"
    
    # each event request is created by a person
    person_requesting = models.ForeignKey('Person',related_name='events_requested',
                                            on_delete=models.CASCADE,null=True)
    
    # event types are manually defined, there are only a few of them
    # yoga, rockclimbing, tango, freediving
    category = models.CharField('type of event',choices=TYPE_CHOICES,default='Yoga',
                                max_length=200)

    # maximum cost (including travel cost) of the class
    max_cost = models.DecimalField(default=0,max_digits=6,decimal_places=0,
                validators=[MinValueValidator(0),DecimalValidator(6,0)])
    
    def __str__(self):
        return self.category
 
