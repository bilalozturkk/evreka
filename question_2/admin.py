from django.contrib import admin

from .models import Bin, Operation, Frequencies
admin.site.register(Bin)
admin.site.register(Operation)
admin.site.register(Frequencies)
