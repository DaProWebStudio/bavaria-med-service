from django.contrib import admin

from .models import Service, ServiceLetter, ClinicService, ServiceCarousel


class ClinicInline(admin.TabularInline):
    model = ClinicService
    extra = 1
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'get_letter')
    exclude = ['slug',]
    inlines = [ClinicInline]


@admin.register(ServiceLetter)
class ServiceLetterAdmin(admin.ModelAdmin):
    exclude = ['letter_en',]


@admin.register(ServiceCarousel)
class ServiceCarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    fieldsets = (
         (None, {
            "fields": ("service", "descriptions")
        }),
    )
    exclude = ['title', 'url']