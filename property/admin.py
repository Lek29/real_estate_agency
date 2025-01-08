from django.contrib import admin

from .models import Flat
from .models import Complaint

class FaltAdmin(admin.ModelAdmin):
    search_fields = [
        'town',
        'address',
        'owner',
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

    raw_id_fields = ['likes']

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat'] 
    list_display = ['user', 'flat', 'text']  
    list_filter = ['flat']  
    search_fields = ['user__username', 'text']  

admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FaltAdmin)
