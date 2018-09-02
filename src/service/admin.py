from django.contrib import admin
from .models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

admin.site.register(Service, ServiceAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_services', 'total', 'created_at', 'created_time_at']


admin.site.register(Receipt, ReceiptAdmin)