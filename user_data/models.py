from django.contrib.gis.db import models
from django.contrib.auth.models import User
from user_data import sms


class Specialty(models.Model):
    name = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "specialties"

def assign_license(user, id):
    responce = requests.get('http://localhost:3000/primary_array')
    data = responce.json()
    (person, license_data) = lookup_license(id, data)
    license = License(user=user,
        license_number=,
        license_name=,

    )
    license.save()
    ext_data = ExtendedUserData(user=user,

    )
    ext_data.save()
    pass

def lookup_license(id, data):
    for person in data:
        for license_data in credentials
            if license_data['ID'] == id:
                return (person, license_data)
    return(None, None)

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



    class Meta:
        verbose_name_plural = "extended user data"
