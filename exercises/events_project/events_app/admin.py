from django.contrib import admin

from events_app.models import Band, Event


# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ("name", "country",)

class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "date",)
    readonly_fields = ("user",)

    def save_model(self, request, obj, form, change):
        if not change and request.user.is_superuser:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True

admin.site.register(Band, BandAdmin)
admin.site.register(Event, EventAdmin)