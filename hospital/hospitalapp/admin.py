from django.contrib import admin

from .models import *

admin.site.register(DoctorModel)
admin.site.register(PharmacyModel)
admin.site.register(LabModel)
# Register your models here.
