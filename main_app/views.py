from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hamster, Toy
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
    id_list = hamster.toys.all().values_list('id')
    toys_hamster_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'hamsters/detail.html', {'hamster': hamster, 'feeding_form': feeding_form, 'toys': toys_hamster_doesnt_have})

class HamsterCreate(CreateView):
  model = Hamster
  fields = '__all__'

class HamsterUpdate(UpdateView):
  model = Hamster
  fields = ['name', 'gender', 'birthday', 'height']

class HamsterDelete(DeleteView):
  model = Hamster
  success_url = '/hamsters'

def add_feeding(request, hamster_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.hamster_id = hamster_id
    new_feeding.save()
  return redirect('detail', hamster_id=hamster_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, hamster_id, toy_id):
  Hamster.objects.get(id=hamster_id).toys.add(toy_id)
  return redirect('detail', hamster_id=hamster_id)

def unassoc_toy(request, hamster_id, toy_id):
  Hamster.objects.get(id=hamster_id).toys.remove(toy_id)
  return redirect('detail', hamster_id=hamster_id)
