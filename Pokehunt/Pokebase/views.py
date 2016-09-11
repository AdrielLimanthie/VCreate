from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .models import Trainer
from .models import Pokemon

# Create your views here.
def index(request):
    context = {}
    return render(request, 'Pokebase/index.html', context)

def register(request):
    context = {}
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            newuser = user_form.save()
            newuser.set_password(newuser.password)
            newuser.save()

            trainer = Trainer(user=newuser, money=0)
            trainer.save()

            registered = True
            context['registered'] = registered
            return render(request, 'registration/register.html', context)
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        context['registered'] = registered
        context['user_form'] = user_form
        return render(request, 'registration/register.html', context)

@login_required(login_url="/login/")
def home(request):
    context = {}
    trainer_id = request.user.profile.id
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    context['trainer'] = trainer
    return render(request, 'Pokebase/home.html', context)

@login_required(login_url="/login/")
def trainerinfo(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    return render(request, 'Pokebase/trainerinfo.html', {'trainer': trainer})

@login_required(login_url="/login/")
def pokemoninfo(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'Pokebase/pokemoninfo.html', {'pokemon': pokemon})