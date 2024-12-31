# Imports
from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from apps.car.models import Car, CarFeature
from apps.car.serializers import CarSerializer
from apps.car.viewsets import CarViewSet


# 
class CarInlineAdmin(admin.TabularInline):
    model = Car.features.through



# Registering the admin
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    serializer_class = CarSerializer
    inlines = (CarInlineAdmin, )
    
        
    # Function to get the features assigned to every car to show them in Admin panel.    
    # format_html_join(sep, format_string, args_generator)    
    @admin.display(description="Features")
    def get_features(self, instance):        
        return format_html_join(
            mark_safe("<br>"),
            "{} {} {} {}",
            (("Feature: ", line.feature.title, " Location: ", line.location) 
             for line in CarFeature.objects.all().order_by('car') 
             if instance.id == line.car.id))
    
        
    list_display = (
        'id',
        'created',
        'updated',
        'manufacturer',
        'model',
        'designation',                        
        'year',
        'type',
        'price',
        'photo',    
        'get_features',
    )
    



