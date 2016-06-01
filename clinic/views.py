from django.shortcuts import get_object_or_404, render
from .models import Patients
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'clinic/index.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        """Return the first five  patients."""
        return Patients.objects.order_by('patid')[:5]

class DetailView(generic.DetailView):
    model = Patients
    template_name = 'clinic/detail.html'
    
# def detail(request, patient_id):
#     patient = get_object_or_404(Patients, pk=patient_id)
#     return render(request, 'clinic/detail.html', {'patient': patient})