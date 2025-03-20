from django.contrib import admin
from django.core.exceptions import ValidationError

from hotel_app.models import Room, Employee, Reservation

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "cleaned",)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ("code", "room",)

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)