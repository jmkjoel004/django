from django.contrib import admin
from .models import People, Event, Attendance

admin.site.register(People)
admin.site.register(Event)
admin.site.register(Attendance)
