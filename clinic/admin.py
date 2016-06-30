from django.contrib import admin
from .models import Patients
# Register your models here.
class PatientsAdmin(admin.ModelAdmin):
	fieldsets = [
	('Personal information',{'fields': ['firstname', 'middlename', 'lastname', 'gender', 'dateofbirth']}),
	('Contact information', {'fields': ['mobilenumber', 'mobilenumber2', 'email']}),
	(None, {'fields': ['guarantor', 'filenumber', 'photolocation','employer_school', 'dueamount', 'insuranceamount', 'balancedue']})
	]
	list_display = ('firstname', 'lastname', 'mobileFormatOk')
	list_filter = ['dateofbirth']
	search_fields = ['lastname']
admin.site.register(Patients, PatientsAdmin)
