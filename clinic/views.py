from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Patients
class IndexView(generic.ListView):
    model = Patients
    template_name = 'clinic/index.html'
    contex_object_name='patients_list'
    def get_queryset(self):
        """Return the first five  patients."""
        return Patients.objects.filter(insuranceamount__gte=20000).order_by('patid')[:]

class DetailView(generic.DetailView):
    model = Patients
    template_name = 'clinic/detail.html'
    def get_queryset(self):
    	"""
    	excludes patients that have insuranceamount
    	below 20000
    	"""
    	return Patients.objects.filter(insuranceamount__gte=20000)

def update(request, pk):
    patients = get_object_or_404(Patients, pk=pk)
    newname = request.POST['lastname']
    patients.lastname=newname
    patients.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('clinic:detail', args=(patients.patid,)))