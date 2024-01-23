from django.contrib import admin
from .models import Plains

class PlainAdmin(admin.ModelAdmin):
    class Meta:
        model = Plains

    list_display = ('name', 'travel_time', 'fromCity', 'toCity')
    list_editable = ('travel_time',)
admin.site.register(Plains, PlainAdmin)