from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['phone_number', 'is_admin', 'is_staff', 'is_active', 'is_seller']
    list_filter = ['is_admin', 'is_staff', 'is_active', 'is_seller']
    fieldsets = [
        (None, {'fields': ('phone_number', 'email', 'name', 'family_name', 'password', 'avatar')}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'is_seller', 'last_login')})

    ]
    add_fieldsets = (
        (None, {'fields': (
            'phone_number', 'email', 'name', 'family_name', 'password1', 'password2',)}),
    )
    search_fields = ['phone_number']
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
