from django.db import models
from django.contrib.auth.models import User

class Specialty(models.Model):
    name = models.TextField(null=False, blank=False)

class License(models.Model):
    DOC = 'DOC'
    NURSE = 'NURSE'
    EMT = 'EMT'
    LICENSE_CLASS_CHOICES = (
      (DOC, 'Physician'),
      (NURSE, 'Nurse'),
      (EMT, 'EMT'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    license_class = models.TextField(choices=LICENSE_CLASS_CHOICES, null=False, blank=False)
    license_name = models.TextField(null=True, blank=True)
    license_number = models.TextField(null=False, blank=False)
    active = models.BooleanField
    initial_date = models.DateField()
    expiration_date = models.DateField()
    zip_code = models.TextField()
    # geography_ : TODO
    specialties = models.ManyToManyField(Specialty)
    record_created = models.DateField(auto_now_add=True)
    record_modified = models.DateField(auto_now=True)
