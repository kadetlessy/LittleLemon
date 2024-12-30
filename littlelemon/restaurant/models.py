from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # id field as primary key
    title = models.CharField(max_length=255)  # Title field
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price field
    inventory = models.IntegerField()  # Inventory field

    def __str__(self):
        return self.title  # Returns the title for a string representation


class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # id field as primary key
    name = models.CharField(max_length=255)  # Name field
    no_of_guests = models.IntegerField()  # No_of_guests field
    booking_date = models.DateTimeField()  # Booking_date field

    def __str__(self):
        return f"{self.name} - {self.booking_date}"  # Returns name and date for string representation
