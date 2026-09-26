from django.db import models


class Organizer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Event(models.Model):
    STATUS_SCHEDULED = 'S'
    STATUS_CANCELLED = 'C'
    STATUS_COMPLETED = 'D'

    STATUS_CHOICES = [
        (STATUS_SCHEDULED, 'Scheduled'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_SCHEDULED
    )
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='events')
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT, related_name='events')

    def __str__(self):
        return self.title


class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class RSVP(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='rsvps')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    rsvp_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('attendee', 'event')

    def __str__(self):
        return f"{self.attendee} -> {self.event}"