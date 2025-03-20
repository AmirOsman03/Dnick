from django.contrib import admin
from .models import Airline,AirlinePilot,Balloon,Flight,Pilot

# Register your models here.

class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'year_of_birth', 'flight_hours', 'rank',)

class BalloonAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'type', 'max_capacity',)

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_founded', 'outside_Europe',)

class AirlinePilotAdmin(admin.TabularInline):
    model = AirlinePilot
    extra = 0

class FlightAdmin(admin.ModelAdmin):
    exclude = ("user",)
    list_display = ("code", "take_off_airport", "land_off_airport", "airline", "pilot", "balloon",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user

    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj = None):
        return False

admin.site.register(Pilot, PilotAdmin)
admin.site.register(Balloon, BalloonAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)
