from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(default=0)
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title