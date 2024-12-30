from django.contrib import admin
from .models import Menu, Booking

# Register your models here.

# Register the Menu model
admin.site.register(Menu)

# Register the Booking model
admin.site.register(Booking)
