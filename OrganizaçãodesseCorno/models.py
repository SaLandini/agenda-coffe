from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class what_I_need_to_do(models.Model):
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
