from django.contrib import admin
from .models import Flat
from .models import Complaint
from .models import Owner


class OwnerInline(admin.TabularInline):  
    model = Owner.properties.through  
    raw_id_fields = ('owner',)  
    extra = 0


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = [
        'town',
        'address',
        'owners__name',
    ]

    readonly_fields = [
        'created_at',
        ]

    list_display = [
        'town',
        'address',
        'price',
        'new_building',
        'construction_year',
    ]

    list_editable = [
        'new_building', 
    ]

    list_filter = [
        'new_building',
        'rooms_number',
        'has_balcony',
    ]

    raw_id_fields = ['likes', 'owners']

    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat'] 
    list_display = ['user', 'flat', 'text']  
    list_filter = ['flat']  
    search_fields = ['user__username', 'text'] 


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'pure_phone']
    search_fields = ['name', 'phonenumbers']

    raw_id_fields = ['flat']
