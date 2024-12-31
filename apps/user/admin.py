# Imports
from django.contrib import admin
from apps.user.models import User




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'photo',            
        'created',
        'updated',
        'user_type',
        'is_staff',
        'is_superuser',
        'is_active'
    )


