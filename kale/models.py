from django.db import models
import datetime
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    # !! login (authentication) details
    # !! phone number
    # !! how they can pay and get paid
    
    
class Venue(models.Model):
    # !! location = (longitude,latitude)
    capacity = models.PositiveIntegerField()
    # !! availability = list of (startDateTime,duration,price)
    
    # Example of a venue: "UNSW Gym Yoga room 2, capacity 25 people, available
    # for rent by the general public Mon and Wed afternoons 2-5pm for $30ph"
    
class Event(models.Model):
    # Events have a many-to-one relationship with Venues. A venue can host many
    # events, but an event can only have one venue.
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE)
    # Events have a many-to-one relationship with Organizers. An organizer can
    # host many events, but an event can only have one organizer.
    organizer = models.ForeignKey(Person,on_delete=models.CASCADE)
    # Manually set a few different types of events for now.
    TYPE_CHOICES = (('Yoga','Yoga'),
                    ('Rockclimbing','Rockclimbing'),
                    ('Tango','Tango'),
                    ('Freediving','Freediving'))
    type = models.CharField('type of event',choices=TYPE_CHOICES,default='Yoga',max_length=200)
    startDateTime = models.DateTimeField()
    duration = models.DurationField()
    # Cost can be up to $999m, specified down to the cent.
    cost = models.DecimalField(max_digits=11,decimal_places=2)
    min_people = models.PositiveIntegerField()
    max_people = models.PositiveIntegerField()
    
    # Example of an event: "Yoga class with Mary on Fri Jan 12th 3pm for one hour
    # in UNSW gym yoga room 2, for up to 20 people, teacher charging $45"
    
    def __str__(self):
        return self.type
 
