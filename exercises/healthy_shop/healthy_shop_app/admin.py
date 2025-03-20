from django.contrib import admin
from healthy_shop_app.models import Category, Product, Client, Sale

# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [ProductInline]

    def has_delete_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        return False

class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change or obj.user is None:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True

class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname",)

class SaleAdmin(admin.ModelAdmin):
    list_display = ("sold_product", "date", "client",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Sale, SaleAdmin)