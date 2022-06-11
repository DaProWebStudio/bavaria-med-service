from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Doctor

admin.site.site_title = 'Админ-панель сайта «Bavaria Med Service»'
admin.site.site_header = 'Админ-панель сайта «Bavaria Med Service»'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'created_at', 'get_photo')
    list_display_links = ('full_name', 'get_photo')
    exclude = ['slug']
    fieldsets = (
         (None, {
            "fields": (("full_name", "position"),)
        }),
         (None, {
            "fields": ("description",)
        }),
         (None, {
            "fields": ("image",)
        }),
    )
    
    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="65">')
    
    get_photo.short_description = 'Миниатюра'

