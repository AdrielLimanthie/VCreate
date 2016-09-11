from django.contrib import admin

# Register your models here.
from .models import Location
from .models import Trainer
from .models import Pokedex
from .models import Pokemon

admin.site.register(Location)
admin.site.register(Trainer)
admin.site.register(Pokedex)
admin.site.register(Pokemon)