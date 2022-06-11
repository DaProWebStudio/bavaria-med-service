from django.contrib import admin

from .models import Statement, Recaptcha


@admin.register(Statement)
class AdminStatement(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'region',  'created_at')


@admin.register(Recaptcha)
class AdminRecaptcha(admin.ModelAdmin):
    list_display = ('answer',)