from django.contrib import admin
from .models import Organizer, Venue, Event, Attendee, RSVP

admin.site.register(Organizer)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(RSVP)