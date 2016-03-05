from rest_framework import serializers
from geocode.models import ZipGeocode


class ZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipGeocode
