from rest_framework import serializers
from apps.agenda.models import Agenda
from apps.contatos.serializers import ContatoSerializer

class AgendaSerializer(serializers.ModelSerializer):
    contato = ContatoSerializer(many=True, read_only=True)
    class Meta:
        model = Agenda
        fields = "__all__"