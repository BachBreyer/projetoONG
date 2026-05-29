# Solicitações de Melhoria

Este documento organiza as tarefas solicitadas durante a evolução do projeto.

## Integração Django e SQLite

### Solicitação

Transformar o projeto estático em um projeto Django com SQLite, seguindo a especificação principal.

### Entregas

- Criação do projeto Django `acitp`.
- Criação do app `core`.
- Configuração do banco SQLite.
- Criação de models, forms, views, URLs e admin.
- Migrações aplicadas.
- Templates HTML integrados ao Django.
- Assets organizados em `static/core`.
- Rotas públicas e painel administrativo funcionando.

## Ajustes de Autenticação e Layout

### Solicitação

- Corrigir a rota `/cadastro/`, que não estava criando conta.
- Criar uma credencial de administrador.
- Padronizar header e footer usando herança de template.
- Fazer o botão de doação em `/voluntariado/` redirecionar para `/doacoes/`.

### Entregas

- Cadastro de usuário corrigido.
- Superusuário criado:
  - Usuário: `admin`
  - Senha: `Admin@12345`
- Criação de `templates/core/base.html`.
- Centralização de header e footer no `base.html`.
- Todos os templates de página passaram a herdar de `base.html`.
- Botão "Fazer uma Doação" em `/voluntariado/` apontando para `/doacoes/`.

## Eventos, Imagens e Admin

### Solicitação

- Exibir em `/eventos/` a imagem enviada no cadastro de eventos e campanhas.
- Inserir a imagem dentro da div `.evento-img`.
- Padronizar a imagem para não distorcer, usando `object-fit`.
- Redirecionar login administrativo para `/admin/`.
- Exibir feedback positivo quando o formulário de `/doacoes/` for enviado com sucesso.
- Mostrar botão "Painel" para usuários autenticados com permissão administrativa.
- Personalizar minimamente o painel `/admin/`.

### Entregas

- Template de eventos renderizando `evento.imagem.url`.
- Fallback visual para eventos sem imagem.
- CSS com `object-fit: cover` para imagens de eventos.
- Evento existente atualizado com imagem padrão para teste.
- Login de usuários administrativos redirecionando para `/admin/`.
- Botão "Painel" visível para usuários staff.
- Feedback positivo visual em `/doacoes/`.
- Personalização mínima do Django Admin.
- Preview de imagem na listagem de eventos no admin.

## Padronização de Fontes e Imagem de Evento

### Solicitação

- Padronizar a fonte do header e footer com as fontes utilizadas em `home.html`.
- Corrigir imagem de evento que ainda não renderizava em `/eventos/`.

### Entregas

- Header e footer padronizados com `Inter`, conforme a Home.
- Diagnóstico do evento cadastrado sem arquivo de imagem.
- Evento existente vinculado a imagem padrão em `media/eventos/`.
- Confirmação de renderização da imagem em `/eventos/`.

