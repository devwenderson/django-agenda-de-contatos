<h1 align="center">Django agenda de contatos</h1>
<p align="center">Agenda de contatos feito com django</p>

## Sobre o projeto
Esse projeto foi desenvolvido para estudar a criação de API REST com Django Rest Framework

### Tecnologias
![Static Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Static Badge](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Static Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Static Badge](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Static Badge](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)

### Ferramentas de desenvolvimento
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Instalação
Clone o repositório
```shell
git clone <link_do_repositório>
```

Execute o docker compose
```shell
docker compose up
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
### Tecnologias
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://docs.djangoproject.com/en/5.2/)
### Configuração do docker-compose
- [Artigo 1](https://dev.to/francescoxx/python-crud-rest-api-using-django-postgres-docker-and-docker-compose-4nhe)
- [Artigo 2](https://www.docker.com/blog/how-to-dockerize-django-app/)
- [Docker com Gunicorn e Nginx](https://github.com/Programador-com-P/django-docker-compose)