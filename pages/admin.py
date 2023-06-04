from django.contrib import admin
from pages.models import Contact, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price')
    list_filter = ['category']
    search_fields = ['product_name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'email', 'timestamp')
    list_filter = ['timestamp']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.site_header = "QR Kafe"
admin.site.index_title = "QR Kafe Yönetim"
admin.site.site_title = "QR Kafe Yönetici"
