from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass
