from rest_framework import serializers
from apps.contatos.models import Email, Telefone, Contato

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__" 

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = "__all__"

class ContatoSerializer(serializers.ModelSerializer):
    email = EmailSerializer(many=True, read_only=True)
    telefone = TelefoneSerializer(many=True, read_only=True)

    class Meta:
        model = Contato
        fields = "__all__"