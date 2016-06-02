from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Patients
class IndexView(generic.ListView):
    template_name = 'clinic/index.html'
    contex_object_name='patients_list'
    def get_queryset(self):
        """Return the first five  patients."""
        return Patients.objects.filter(insuranceamount__gte=20000).order_by('patid')[:]

class DetailView(generic.DetailView):
    model = Patients
    template_name = 'clinic/detail.html'