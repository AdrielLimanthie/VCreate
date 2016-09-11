from django.db import models
from django.contrib.auth.models import User
from Pokehunt import settings
import os

class Location(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Trainer(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    money = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    title = models.CharField(max_length=50) # might need to be improved
    def __str__(self):
        return self.user.username

class Pokedex(models.Model):
    name = models.CharField(max_length=25)
    dexnumber = models.PositiveSmallIntegerField(default=0)
    type1 = models.CharField(max_length=10, null=True, blank=True)     # might need to be improved
    type2 = models.CharField(max_length=10, null=True, blank=True)
    base_power = models.PositiveIntegerField(default=1)
    location = models.ManyToManyField(Location)
    picture = models.ImageField(upload_to = os.path.join(settings.STATICFILES_DIRS[0], 'img'), null=True)
    def __str__(self):
        return self.name

class Pokemon(models.Model):
    species = models.ForeignKey(Pokedex, on_delete=models.PROTECT)
    owner = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=25)
    level = models.PositiveSmallIntegerField(default=1)
    gender = models.PositiveSmallIntegerField(default=1)    # 1: Male 2:Female 0:NoGender
    exp = models.PositiveIntegerField(default=0)
    # held_item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    power = models.PositiveIntegerField(default=1)
    iv = models.PositiveSmallIntegerField(default=0)
    # nature = 
    # ability =
    # moves
    # ev iv
    # ot (might be implemented later)
    def __str__(self):
        return self.nickname
