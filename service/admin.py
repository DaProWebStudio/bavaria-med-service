from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceNews(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    exclude = ['slug', 'image']
