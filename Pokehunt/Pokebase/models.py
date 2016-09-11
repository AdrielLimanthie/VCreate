from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    # trainer_name = models.CharField(max_length=100)
    trainer_money = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class Pokemon(models.Model):
    owner = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    pokemon_name = models.CharField(max_length=25)
    pokemon_level = models.IntegerField(default=1)
    def __str__(self):
        return self.pokemon_name