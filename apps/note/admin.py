from django.contrib import admin

from core.models import SaleNote


@admin.register(SaleNote)
class SaleNoteAdmin(admin.ModelAdmin):
    list_display = ('created', 'address', 'price', 'deposit', 'rent', 'owner', 'owner_number', 'state', 'realty_type')

    @staticmethod
    def realty_type(self, obj):
        if not obj.realty_type.type:
            return ""
        return str(obj.realty_type.type)
