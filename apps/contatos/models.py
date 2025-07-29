from django.db import models
from apps.agenda.models import Agenda

class Contato(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=50)
    agenda = models.ForeignKey(Agenda, related_name='contato', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return f"{self.name} - {self.telefone}"

class Email(models.Model):
    email = models.CharField(verbose_name="Email", max_length=255)
    contato = models.ForeignKey(Contato, related_name='email', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"
    
    def __str__(self):
        return f"{self.email}"

class Telefone(models.Model):
    telefone = models.CharField(verbose_name="Telefone", max_length=15)
    contato = models.ForeignKey(Contato, related_name='telefone', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.telefone}"




