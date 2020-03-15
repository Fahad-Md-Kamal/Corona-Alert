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
