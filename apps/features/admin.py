# Imports
from django.contrib import admin
from apps.features.models import Feature




@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'updated',            
        'photo',  
        'designation',
        'title',
        'description',    
    )


