from django.conf.urls import url

from . import views

app_name = "Pokebase"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^trainer/(?P<trainer_id>[0-9]+)/$', views.trainerinfo, name='trainerinfo'),
    url(r'^pokemon/(?P<pokemon_id>[0-9]+)/$', views.pokemoninfo, name='pokemoninfo'),
]