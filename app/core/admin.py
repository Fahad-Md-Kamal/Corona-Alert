from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from core import models

admin.site.register(models.User)
admin.site.register(models.Followup)

@admin.register(models.Patient)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('first_name', 'last_name', 'location')
