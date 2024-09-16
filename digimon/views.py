from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Digimon, Move

class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

@login_required
def digimon_index(request):
    digimons = Digimon.objects.filter(user=request.user)
    return render(request, 'digimons/index.html', {'digimons': digimons})

@login_required
def digimon_detail(request, digimon_id):
    digimon = Digimon.objects.get(id=digimon_id)
    moves_digimon_doesnt_have = Move.objects.exclude(id__in = digimon.moves.all().values_list('id'))
    return render(request, 'digimons/detail.html', {
        'digimon': digimon,
        'moves': moves_digimon_doesnt_have
        })

class DigimonCreate(LoginRequiredMixin, CreateView):
    model = Digimon
    fields = ['digid', 'name', 'level', 'attribute', 'type', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DigimonUpdate(LoginRequiredMixin, UpdateView):
    model = Digimon
    fields = ['digid', 'name', 'level', 'attribute', 'type', 'description']

class DigimonDelete(LoginRequiredMixin, DeleteView):
    model = Digimon
    success_url = '/digimons/'

class MoveCreate(LoginRequiredMixin, CreateView):
    model = Move
    fields = '__all__'

class MoveList(LoginRequiredMixin, ListView):
    model = Move

class MoveDetail(LoginRequiredMixin, DetailView):
    model = Move

class MoveUpdate(LoginRequiredMixin, UpdateView):
    model = Move
    fields = ['name', 'description']

class MoveDelete(LoginRequiredMixin, DeleteView):
    model = Move
    success_url = '/moves/'


@login_required
def associate_move(request, digimon_id, move_id):
    Digimon.objects.get(id=digimon_id).moves.add(move_id)
    return redirect('digimon_detail', digimon_id=digimon_id)

@login_required
def remove_move(request, digimon_id, move_id):
    Digimon.objects.get(id=digimon_id).moves.remove(move_id)
    return redirect('digimon_detail', digimon_id=digimon_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('digimon_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
