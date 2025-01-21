from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username','email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'address'
                           , 'city', 'state', 'country','pincode'),
            },
        ),
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Info',
            {
                'fields': (
                    'phone',
                    'address',
                    'city',
                    'state',
                    'country',
                    'pincode',
                )
            }
        )
    ) 

admin.site.register(User, CustomUserAdmin)