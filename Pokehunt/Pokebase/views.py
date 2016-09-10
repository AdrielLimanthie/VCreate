from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Trainer
from .models import Pokemon

# Create your views here.
def index(request):
    context = {}
    return render(request, 'Pokebase/index.html', context)

@login_required(login_url="/login/")
def home(request):
    trainer_id = request.user.profile.id
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    return render(request, 'Pokebase/home.html', {'trainer': trainer})

@login_required(login_url="/login/")
def trainerinfo(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    return render(request, 'Pokebase/trainerinfo.html', {'trainer': trainer})

@login_required(login_url="/login/")
def pokemoninfo(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'Pokebase/pokemoninfo.html', {'pokemon': pokemon})