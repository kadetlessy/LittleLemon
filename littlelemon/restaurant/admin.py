from django.contrib import admin
from .models import MenuItem, Booking

# Register your models here.

# Register the Menu model
admin.site.register(MenuItem)

# Register the Booking model
admin.site.register(Booking)
