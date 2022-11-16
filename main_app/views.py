from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hamster
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def hamster_index(request):
    hamsters = Hamster.objects.all()
    return render(request, 'hamsters/index.html', {'hamsters': hamsters})

def hamsters_detail(request, hamster_id):
    hamster = Hamster.objects.get(id=hamster_id)
    feeding_form = FeedingForm()
    return render(request, 'hamsters/detail.html', {'hamster': hamster, 'feeding_form': feeding_form})

class HamsterCreate(CreateView):
  model = Hamster
  fields = '__all__'

class HamsterUpdate(UpdateView):
  model = Hamster
  fields = ['breed', 'description', 'age']

class HamsterDelete(DeleteView):
  model = Hamster
  success_url = '/hamsters'
