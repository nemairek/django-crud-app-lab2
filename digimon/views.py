from django.shortcuts import render
from .models import Digimon

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