from django.contrib import admin

from core.models import PoliceProfile, StationPolice

class StationPoliceAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','police_code','created_date','edited_date')
	search_fields=['first_name','last_name','police_code']

class PoliceProfileAdmin(admin.ModelAdmin):
	list_display=('police','station','phone_number','email','created_date')
	search_fields=['police__username','police__first_name','police__last_name','station__name','phone_number','email']

admin.site.register(StationPolice,StationPoliceAdmin)
admin.site.register(PoliceProfile,PoliceProfileAdmin)
