from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Hamster

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def hamster_index(request):
    hamsters = Hamster.objects.all()
    return render(request, 'hamsters/index.html', {'hamsters': hamsters})

def hamsters_detail(request, hamster_id):
    hamster = Hamster.objects.get(id=hamster_id)
    return render(request, 'hamsters/detail.html', {'hamster': hamster})

class HamsterCreate(CreateView):
  model = Hamster
  fields = '__all__'
