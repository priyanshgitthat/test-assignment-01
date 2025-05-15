from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': (
                'user_type',
                'profile',
                'addressLine1',
                'city',
                'state',
                'pincode',
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {
            'fields': (
                'user_type',
                'profile',
                'addressLine1',
                'city',
                'state',
                'pincode',
            )
        }),
    )



admin.site.register(CustomUser,CustomUserAdmin)