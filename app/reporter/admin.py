from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin


from reporter import models

@admin.register(models.Incidence)
class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ['name', 'location']

