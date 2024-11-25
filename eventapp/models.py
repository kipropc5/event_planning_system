# from django.db import models
# from django.core.exceptions import ValidationError
# from datetime import timedelta
#
#
# # Create your models here.
# class Event(models.Model):
#     event_name = models.CharField(max_length=100)
#     event_description = models.CharField(max_length=255)  # Increased length
#     event_location = models.CharField(max_length=255)  # Increased length
#     start_time = models.TimeField(null=False)
#     end_time = models.TimeField(null=False)
#     event_date = models.DateField(null=False)
#     event_organizer = models.CharField(max_length=255)  # Increased length
#
#     def clean(self):
#         if self.end_time <= self.start_time:
#             raise ValidationError('End time must be after start time')
#
#     def __str__(self):
#         return self.event_name
#
#
# class Participant(models.Model):
#     participant_name = models.CharField(max_length=100)
#     participant_email = models.CharField(max_length=100)
#     event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.participant_name
from django.db import models
from django.core.exceptions import ValidationError

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.CharField(max_length=255)
    event_location = models.CharField(max_length=255)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    event_date = models.DateField(null=False)
    event_organizer = models.CharField(max_length=255)

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('End time must be after start time')

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['event_date', 'start_time']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class Participant(models.Model):
    participant_name = models.CharField(max_length=100)
    participant_email = models.EmailField(max_length=100)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return self.participant_name

    class Meta:
        ordering = ['participant_name']
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'

