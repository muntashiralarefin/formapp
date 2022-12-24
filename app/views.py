from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import VenueForm

# Create your views here.
def home(request):
    submitted = False

    if request.method =="POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home.html', {'form': form, 'submitted':submitted})
