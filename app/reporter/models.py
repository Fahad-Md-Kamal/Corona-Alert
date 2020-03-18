from __future__ import unicode_literals
from django.contrib.gis.db import models

class Incidence(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField()
    objects = models.Manager()

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name 


class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    city_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.counties