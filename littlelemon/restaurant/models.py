from django.db import models

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)  # id field as primary key
    title = models.CharField(max_length=255)  # Title field
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price field
    inventory = models.SmallIntegerField()  # Inventory field

    def __str__(self):
        return self.title  # Returns the title for a string representation

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # id field as primary key
    name = models.CharField(max_length=255)  # Name field
    no_of_guests = models.IntegerField()  # No_of_guests field
    booking_date = models.DateTimeField()  # Booking_date field

    def __str__(self):
        return f"{self.name} - {self.booking_date}"  # Returns name and date for string representation
