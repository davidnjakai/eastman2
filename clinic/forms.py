from django import forms
from django.forms import ModelForm
from .models import Patients

class PatientsForm(ModelForm):
	class Meta:
		model = Patients
		fields = '__all__'