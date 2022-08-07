from django.contrib import admin

# Register your models here.
from realty.models import RealtyType


@admin.register(RealtyType)
class RealtyAdmin(admin.ModelAdmin):
    list_display = ("id", "type")
