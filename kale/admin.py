from django.contrib import admin

from .models import Person, Location, CalendarSlot, VenueSlot, Venue, Event, EventRequest

# Register your models here.
admin.site.register(Person)
admin.site.register(Location)
admin.site.register(CalendarSlot)
admin.site.register(VenueSlot)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(EventRequest)
