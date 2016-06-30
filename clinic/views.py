from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Patients
from .forms import PatientsForm

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

def patdetails(request, pk):
    patients = Patients.objects.get(pk = pk)
    if request.method == "POST":
        form = PatientsForm(request.POST, instance=patients)
        if form.is_valid():
            ourpatient = form.save(commit = False)
            ourpatient.save()
            return HttpResponseRedirect(reverse('clinic:detail', args=(ourpatient.patid,)))
    else:
        form = PatientsForm(instance = patients)
    return render(request, 'clinic/edit.html', {'form': form, 'patients': patients})

def delete(request, pk):
    patients = Patients.objects.get(pk = pk)
    patients.delete()
    return HttpResponseRedirect(reverse('clinic:deleted'))

def deleted(request):
    return render(request, 'clinic/deleted.html', {'notification':"PATIENT DELETED"})

def add(request):
    if request.method == "POST":
        form = PatientsForm(request.POST)
        if form.is_valid():
            ourpatient=form.save()
            return HttpResponseRedirect(reverse('clinic:index'))
    else:
        form = PatientsForm()
    return render(request, 'clinic/edit.html', {'form': form})
