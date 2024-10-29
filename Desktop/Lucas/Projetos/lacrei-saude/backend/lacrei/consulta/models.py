from django.db import models
from profissional.models import Profissional

class Consulta(models.Model):
    data = models.DateField()
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Consulta em {self.data} com {self.profissional.nome}"