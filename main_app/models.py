from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

SEASONS = (
    ('AL', 'All'),
    ('WT', 'Winter'),
    ('SP', 'Spring'),
    ('SM', 'Summer'),
    ('FL', 'Fall'),
)

ACTIVITIES = (
    ("AL", "All"),
    ("BP", "Backpacking"),
    ("BS", "Business"),
    ("LS", "Leisure"),
    ("SS", "Sightseeing"),
    ("OT", "Other")
)

AGES = (
    ("A", "All Ages"),
    ("I", "Infant"),
    ("C", "Child"),
    ("T", "Teen"),
    ("A", "Adult"),
    ("S", "Senior")
)

GENDERS = (
    ("A", "All"),
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other")
)

CATEGORIES = (
    ("CL", "Clothing"),
    ("EL", "Electronics"),
    ("EQ", "Equipment"),
    ("PS", "Personal"),
    ("MD", "Medication"),
    ("OT", "Other"),
)


class Item (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    season = models.CharField(max_length=25, choices=SEASONS, default=SEASONS[0][1])
    activity = models.CharField(max_length=25, choices=ACTIVITIES, default=ACTIVITIES[0][1])
    age = models.CharField(max_length=25, choices=AGES, default=AGES[0][1])
    gender = models.CharField(max_length=25, choices=GENDERS, default=GENDERS[0][1])
    vote = models.IntegerField(default=0)
    category = models.CharField(max_length=25, choices=CATEGORIES)
    trip_id = models.IntegerField(null=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return (f"{self.get_season_display()} on {self.name}")

    # sort by voting
    class Meta:
        ordering = ['-vote']


    # Link the user
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Trip(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    season = models.CharField(max_length=25, choices=SEASONS, default=SEASONS[0][1])
    # activity = models.CharField(max_length=50, default=activity[0][1])
    travelers = models.CharField(max_length=50, default='')
    # num_items = models.IntegerField(default=15)


class Activity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activity = models.CharField(max_length=50, default=ACTIVITIES[0][1])
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)


class Traveler(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25, choices=GENDERS, default=GENDERS[0][1])
    age = models.CharField(max_length=25, choices=AGES, default=AGES[0][1])
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)


def getChoices(choices):
    return [x[1] for x in choices]
