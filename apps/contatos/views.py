from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.contatos.models import Email, Telefone, Contato
from apps.contatos.serializers import EmailSerializer, TelefoneSerializer, ContatoSerializer

@api_view(['GET', 'POST'])
def contato_list(request):
    if request.method == 'GET':
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(contatos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ContatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def email_list(request):
    if request.method == 'GET':
        emails = Email.objects.all()
        serializer = EmailSerializer(emails, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        email_serializer = EmailSerializer(data=request.data)
        if email_serializer.is_valid():
            email_serializer.save()
            return Response(email_serializer.data, status=status.HTTP_201_CREATED)
        return Response(email_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def telefone_list(request):
    if request.method == 'GET':
        telefones = Telefone.objects.all()
        serializer = TelefoneSerializer(telefones, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TelefoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
