from django.contrib import admin

# Register your models here.
from .models import Pokemon
from .models import Trainer

admin.site.register(Pokemon)
admin.site.register(Trainer)