from django.contrib import admin

from car_service_app.models import Manufacturer, Car, Workshop, Service


# Register your models here.

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        return request.user.is_superuser

class CarAdmin(admin.ModelAdmin):
    list_display = ('type','max_speed',)

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_founded', 'old_timer',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user

    def has_change_permission(self, request, obj = None):
        return False

    def has_delete_permission(self, request, obj = None):
        return False

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('code', 'date', 'user', 'car', 'workshop',)
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Service, ServiceAdmin)