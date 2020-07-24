from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Semana(models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=100, default='SOME STRING')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'what'

    def str(self):
        return self.titulo
        
    def ti_me(self):
        return self.time


class Tarefas(models.Model):
    materia = models.CharField(max_length=100)
    dia_entrega = models.CharField(max_length=10, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'etec'


class Anotas(models.Model):
    notas = models.CharField(max_length=100)
    descri = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'nota'


class Estudos(models.Model):
    youtube = models.BooleanField(editable=True)
    curso_link = models.CharField(max_length=200)
    curso_name = models.CharField(max_length=200)
    curso_site_name = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cursos'