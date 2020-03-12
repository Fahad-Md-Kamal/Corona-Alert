from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import User, Shop

admin.site.register(User)
