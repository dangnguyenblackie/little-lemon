from django.db import models

# Booking Table
class BookingTable (models.Model):
    name        = models.CharField(max_length=255)
    noOfGuests  = models.IntegerField()
    bookingDate = models.DateField()

# Menu Table
class MenuTable (models.Model):
    title       = models.CharField(max_length=255)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    inventory   = models.IntegerField()