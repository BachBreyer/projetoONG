# projetoONG

Sistema web da ACITP - A Casa do Idoso para Todos os Povos, agora integrado com Django e SQLite.

## Especificações

Os documentos de especificação do projeto ficam em [specs](specs/):

- [Especificação principal](specs/project-specification.md)
- [Solicitações de melhoria](specs/change-requests.md)

## Como rodar

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## Rotas principais

- `/` - Home
- `/historia/` - Nossa historia
- `/eventos/` - Eventos e campanhas
- `/doacoes/` - Informacoes de doacao e registro de doacoes
- `/voluntariado/` - Cadastro de voluntarios
- `/depoimentos/` - Depoimentos
- `/transparencia/` - Prestacao de contas
- `/admin/` - Administracao Django

Para criar um administrador:

```bash
.venv/bin/python manage.py createsuperuser
```
