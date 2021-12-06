from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

User = get_user_model()

admin.site.register(Permission)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = [
        [None, {'fields': ['username', 'password']}],
        [_('Personal info'), {'fields': ['first_name', 'last_name', 'email']}],
        [_('Permissions'), {
            'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'],
        }],
        [_('Important dates'), {'fields': ['last_login', 'date_joined']}],
    ]
