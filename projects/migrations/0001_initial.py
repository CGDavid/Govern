# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-15 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacio_responsabilitat', models.PositiveSmallIntegerField()),
                ('puntuacio_estrategia', models.PositiveSmallIntegerField()),
                ('puntuacio_adquisicio', models.PositiveSmallIntegerField()),
                ('puntuacio_rendiment', models.PositiveSmallIntegerField()),
                ('puntuacio_conformitat', models.PositiveSmallIntegerField()),
                ('puntuacio_conducta', models.PositiveSmallIntegerField()),
                ('comentari_responsabilitat', models.TextField()),
                ('comentari_estrategia', models.TextField()),
                ('comentari_adquisicio', models.TextField()),
                ('comentari_rendiment', models.TextField()),
                ('comentari_conformitat', models.TextField()),
                ('comentari_conducta', models.TextField()),
                ('creat', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificat', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Metrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('descripcio', models.TextField()),
                ('unitat', models.CharField(choices=[('EUR', 'Euros'), ('DIA', 'Dies'), ('PCT', 'Percentatge')], max_length=11)),
                ('maxim', models.PositiveSmallIntegerField(null=True)),
                ('minim', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objectiu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('descripcio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Principi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('objectiu', models.ManyToManyField(related_name='principis_objectius', to='projects.Objectiu')),
            ],
        ),
        migrations.CreateModel(
            name='Projecte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('descripcio', models.TextField()),
                ('presupost', models.FloatField()),
                ('estat', models.CharField(choices=[('PE', 'Pendent'), ('PR', 'Progres'), ('RE', 'Rebutjat'), ('FI', 'Finalitzat')], max_length=2)),
                ('tipus', models.CharField(choices=[('F2P', 'Free To Play'), ('CO', 'Convencional'), ('ALT', 'Altres')], default='CO', max_length=2)),
                ('creat', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificat', models.DateTimeField(auto_now=True, null=True)),
                ('data_inici', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_fi', models.DateTimeField(auto_now=True, null=True)),
                ('maxim', models.PositiveSmallIntegerField(null=True)),
                ('minim', models.PositiveSmallIntegerField(null=True)),
                ('objectiu', models.ManyToManyField(related_name='projectes_objectius', to='projects.Objectiu')),
            ],
        ),
        migrations.AddField(
            model_name='metrica',
            name='objectiu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metriques_objectius', to='projects.Objectiu'),
        ),
        migrations.AddField(
            model_name='evaluacio',
            name='projecte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projecte'),
        ),
    ]
