from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.contatos.views import contato_list, email_list, telefone_list

urlpatterns = [
    path('contatos/', contato_list),
    path('emails/', email_list),
    path('telefones/', telefone_list),
]
