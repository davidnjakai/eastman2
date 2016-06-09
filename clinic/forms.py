from django import forms
from django.forms import ModelForm
from .models import Patients
from django.forms import SelectDateWidget
import datetime

class PatientsForm(ModelForm):
	class Meta:
		model = Patients
		fields = '__all__'
		YEARCHOICES=(range(datetime.date.today().year - 100, datetime.date.today().year))
		widgets = {
            'dateofbirth': SelectDateWidget(years = YEARCHOICES),
        }