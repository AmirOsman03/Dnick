from django.contrib import admin

from market_app.models import Contact, Market, Employee, Product, MarketProduct


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("street", "street_number",)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "surname",)
    readonly_fields = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)

    list_filter = ("type", "homemade",)


class MarketProductAdmin(admin.TabularInline):
    list_display = ("market", "product", "quantity",)

    model = MarketProduct
    extra = 0


class MarketAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ("user",)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    inlines = [MarketProductAdmin]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
