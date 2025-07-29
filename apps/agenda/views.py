from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.agenda.serializers import AgendaSerializer
from apps.agenda.models import Agenda

@api_view(['GET', 'POST'])
def agenda_list(request):
    if request.method == 'GET':
        agenda = Agenda.objects.all()
        serializer = AgendaSerializer(agenda, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AgendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
