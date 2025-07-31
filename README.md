<h1 align="center">Django agenda de contatos</h1>
<p align="center">Agenda de contatos feito com django</p>

## Sobre o projeto
Esse projeto foi desenvolvido para estudar a criação de API REST com Django Rest Framework

### Tecnologias
<p display="inline-block">
    <img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/django.png" alt="Django" title="Django"/>
</p>


### Ferramentas de desenvolvimento
<div>
    <img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/visual_studio_code.png" alt="Visual Studio Code" title="Visual Studio Code"/>
</div>

## Instalação
Clone o repositório
```shell
git clone <link_do_repositório>
```

Crie uma venv
```shell
# Linux
python3 -m venv .venv

# Windows
python -m venv .venv
```

Ative a venv
```shell
# Linux
source .venv/bin/activate

# Windows (Powershell)
.venv\Scripts\Activate.ps1
```

Instale as dependências
```shell
pip install -r requirements.txt
```

Faça as migrações
```shell
python manage.py makemigrations

python manage.py migrate
```

Inicie o servidor local
```shell
python manage.py runserver
```

## Execução
### Padrão dos JSON
Agenda
```json
{
    "id": number,
    "contatos": []
}
```

Contato
```json
{
    "id": number,
    "telefones": [],
    "emails": [],
}
```

Email
```json
{
    "id": number,
    "email": str,
    "contato": number
}
```

Telefone
```json
{
    "id": number,
    "telefone": str,
    "contato": number
}
```

### Rotas da API:
#### Rotas `GET`
- `GET /api/contatos/` - Lista os contatos
- `GET /api/telefones/` - Lista os telefones
- `GET /api/emails/` - Lista os emails
- `GET /api/agendas/` - Lista as agendas

#### Rotas `POST`
- `POST /api/contatos/` - Cria um contato
- `POST /api/telefones/` - Cria telefone
- `POST /api/emails/` - Cria email
- `POST /api/agendas/` - Cria agenda



## Referências
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://docs.djangoproject.com/en/5.2/)