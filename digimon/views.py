from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Digimon, Move

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def digimon_index(request):
    digimons = Digimon.objects.all()  
    return render(request, 'digimons/index.html', {'digimons': digimons})

def digimon_detail(request, digimon_id):
    digimon = Digimon.objects.get(id=digimon_id)
    return render(request, 'digimons/detail.html', {'digimon': digimon})

class DigimonCreate(CreateView):
    model = Digimon
    fields = '__all__'

class DigimonUpdate(UpdateView):
    model = Digimon
    fields = ['digid', 'name', 'level', 'attribute', 'type', 'description']

class DigimonDelete(DeleteView):
    model = Digimon
    success_url = '/digmons/'

class MoveCreate(CreateView):
    model = Move
    fields = '__all__'

