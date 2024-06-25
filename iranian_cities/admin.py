from django.contrib import admin
from django.contrib.admin import widgets
from iranian_cities.models import (
    Ostan, Shahrestan, Shahr,
)

class IranianCitiesAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        db = kwargs.get('using')
        kwargs['widget'] = widgets.ForeignKeyRawIdWidget(
            db_field.remote_field, self.admin_site, using=db)

        if 'queryset' not in kwargs:
            queryset = self.get_field_queryset(db, db_field, request)
            if queryset is not None:
                kwargs['queryset'] = queryset

        return db_field.formfield(**kwargs)

@admin.register(Ostan)
class OstanAdmin(admin.ModelAdmin):
    list_display = ['name', 'amar_code']
    search_fields = ['name', 'amar_code']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Shahrestan)
class ShahrestanAdmin(admin.ModelAdmin):
    list_display = ['name', 'amar_code', 'ostan']
    list_filter = ['ostan']
    search_fields = ['name', 'amar_code', 'ostan__name']
    raw_id_fields = ['ostan']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Shahr)
class ShahrAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'amar_code', 'shahr_type',
         'shahrestan', 'ostan'
    ]
    list_filter = ['ostan']
    search_fields = [
        'name', 'amar_code', 'shahr_type',
        'shahrestan__name', 'ostan__name'
    ]
    raw_id_fields = ['shahrestan', 'ostan']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False




