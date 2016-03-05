from django.contrib.gis.db import models
from django.contrib.auth.models import User
from user_data import sms


class Specialty(models.Model):
    name = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "specialties"


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

    specialties = models.ManyToManyField(Specialty)
    record_created = models.DateField(auto_now_add=True)
    record_modified = models.DateField(auto_now=True)


class ExtendedUserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    zip_code = models.TextField()
    phone = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    location = models.PointField()

    def send_message_to(self, msg):
        print(sms.send_message_to(self.phone, msg))

    @classmethod
    def find_license(self, user):
        # Look up user's license from license API server,
        # create a new ExtendedUserData instance,
        # associate it to `user`
        pass

    class Meta:
        verbose_name_plural = "extended user data"
