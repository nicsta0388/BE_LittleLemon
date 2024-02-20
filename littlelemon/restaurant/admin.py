from django.contrib import admin

# Register your models here.

from .models import Booking, MenuItem, Menu, Employees


admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(Employees)