from django.contrib import admin

# Register your models here.

from .models import Vehicle, NavigationRecord

admin.site.register(Vehicle)
admin.site.register(NavigationRecord)
