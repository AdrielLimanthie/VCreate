# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-12 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pokebase', '0007_pokedex_dexnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('group', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='type1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='type2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='bag',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pokebase.Item'),
        ),
        migrations.AddField(
            model_name='bag',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pokebase.Trainer'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='held_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Pokebase.Bag'),
        ),
    ]