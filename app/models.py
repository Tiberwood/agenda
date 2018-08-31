# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    ADMIN = 'Administrador'
    USUARIO = 'Usuario'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    OPCIONES = (
        (ADMIN, 'Administrador'),
        (USUARIO, 'Usuario'))
    role = models.CharField(choices=OPCIONES, null = True, blank=True, max_length=255)        

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Sala(models.Model):
    nombre = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
    
    def __str__(self):
        return self.nombre + ' ' + self.ubicacion + ' ' + self.capacidad + ' ' + self.estado    
    
class Insumo(models.Model):
    nombre = models.CharField(max_length=255)
        
    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'
    
    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    insumo = models.ManyToManyField(Insumo)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fechainicio = models.DateField(default=datetime.datetime.today)
    cantidadpersonas = models.PositiveIntegerField()
    nodisponible = 'No disponible'
    disponible = 'Disponible'
    reservada = 'Reservada'
    confirmada = 'Confirmada'
    OPCIONES = (
        (nodisponible, 'No disponible'),
        (disponible, 'Disponible'), 
        (reservada, 'Reservada'), 
        (confirmada, 'Confirmada'),
        )
    estado = models.CharField(choices=OPCIONES, max_length=255, default='Disponible')
    horainicio = models.TimeField()
    horafin = models.TimeField()