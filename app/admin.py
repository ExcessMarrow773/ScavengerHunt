from django.contrib import admin
from app.models import request
# Register your models here.

@admin.register(request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('device', 'created_on')
    list_filter = ('created_on',)
    date_hierarchy = 'created_on'