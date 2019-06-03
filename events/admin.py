from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['course', 'event_date', 'title', 'status']
    list_filter = ['course', 'status']
    
    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)
