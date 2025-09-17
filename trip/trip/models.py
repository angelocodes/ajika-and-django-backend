from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

#trips & notes (images)

class Trip(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=2) # USA -> US
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return f"{self.city}, {self.country}"
    
class Note(models.Model):
    EXCURSIONS = (
        ('sightseeing', 'Sightseeing'),
        ('hiking', 'Hiking'),
        ('beach', 'Beach'),
        ('cultural', 'Cultural'),
        ('adventure', 'Adventure'),
        ('relaxation', 'Relaxation'),
        ('other', 'Other'),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=100, choices=EXCURSIONS, blank=True)
    img = models.ImageField(upload_to='notes', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.name} - Note for {self.trip.city} on {self.trip.start_date} to {self.trip.end_date}"