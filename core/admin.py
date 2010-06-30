from django.contrib import admin

from core.models import PoliceProfile, StationPolice

admin.site.register(StationPolice)
admin.site.register(PoliceProfile)