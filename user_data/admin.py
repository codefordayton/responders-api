from django.contrib import admin
from user_data.models import ExtendedUserData, License, Specialty


class ExtendedUserDataAdmin(admin.ModelAdmin):
    pass


class LicenseAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExtendedUserData, ExtendedUserDataAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Specialty, SpecialtyAdmin)