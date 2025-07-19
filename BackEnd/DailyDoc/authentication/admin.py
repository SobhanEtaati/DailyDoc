from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Used to allow field names to be translated in admin UI (nice for international projects)
from django.utils.translation import gettext_lazy as _

# We want the admin to behave correctly, because we have Custom User Model
class UserAdmin(BaseUserAdmin):

    # Sorts users by email by default
    ordering = ['email']

    # Controls which fields show in the admin user list table
    list_display = ['email', 'first_name', 'last_name', 'is_staff']

    # Lets you search users by email from the admin search bar
    search_fields = ['email']

    # Controls the layout of the "Edit User" form in the admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login',)}),
    )

    # This controls the form layout for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

    readonly_fields = ['email']
    

admin.site.register(User, UserAdmin)
