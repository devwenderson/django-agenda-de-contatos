from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.agenda.views import agenda_list

urlpatterns = [
    path('agendas/', agenda_list)
]
