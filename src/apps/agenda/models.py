from django.db import models

class Agenda(models.Model):

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"

    def __str__(self):
        return "Agenda"

