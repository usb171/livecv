from django.db import models
from django.contrib.auth.models import User

class Sala(models.Model):
    nome = models.CharField('Nome', max_length=20, null=True)
    usuarios = models.ManyToManyField(User, blank=True)
    # usuarios = models.OneToMany(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return self.nome
