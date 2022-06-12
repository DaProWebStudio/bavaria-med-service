from django.contrib import admin

from .models import ClinicService, Service, ServiceCarousel


class ClinicInline(admin.TabularInline):
    model = ClinicService
    extra = 1
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    exclude = ['slug',]
    inlines = [ClinicInline]


@admin.register(ServiceCarousel)
class ServiceCarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    fieldsets = (
         (None, {
            "fields": ("service", "descriptions")
        }),
    )
    exclude = ['title', 'url']