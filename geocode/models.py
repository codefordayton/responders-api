from django.contrib.gis.db import models


class ZipGeocode(models.Model):
    zip = models.TextField(primary_key=True)
    city = models.TextField()
    state = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timezone = models.IntegerField()
    daylight_savings = models.BooleanField()

    class Meta:
        db_table = 'zip_geocode'
