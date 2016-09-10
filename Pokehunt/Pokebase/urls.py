from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = "Pokebase"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'), 
    url(r'^home/$', views.home, name='home'),
    url(r'^trainer/(?P<trainer_id>[0-9]+)/$', views.trainerinfo, name='trainerinfo'),
    url(r'^pokemon/(?P<pokemon_id>[0-9]+)/$', views.pokemoninfo, name='pokemoninfo'),
]