from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Testimonial,
    Doacao,
    Event,
    Instituicao,
    MensagemContato,
    PrestacaoConta,
    Voluntario,
)


@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'atualizado_em']
    search_fields = ['nome', 'email', 'telefone']


@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'profissao', 'status', 'criado_em']
    list_filter = ['status', 'profissao', 'criado_em']
    search_fields = ['nome', 'email', 'telefone']


@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'doador_nome', 'valor', 'item_doado', 'data', 'registrado_por']
    list_filter = ['tipo', 'data']
    search_fields = ['doador_nome', 'doador_email', 'descricao', 'item_doado']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "starts_at", "is_featured", "is_active")
    list_filter = ("is_featured", "is_active", "starts_at")
    search_fields = ("title", "location", "description")
    ordering = ("starts_at",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_role", "is_featured", "is_active")
    list_filter = ("is_featured", "is_active")
    search_fields = ("author_name", "author_role", "content")


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'assunto', 'respondida', 'criada_em']
    list_filter = ['respondida', 'criada_em']
    search_fields = ['nome', 'email', 'assunto']


@admin.register(PrestacaoConta)
class PrestacaoContaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'periodo_inicio', 'periodo_fim', 'valor_arrecadado', 'valor_utilizado', 'publicado']
    list_filter = ['publicado', 'periodo_fim']
    search_fields = ['titulo', 'resumo']


admin.site.site_header = 'Painel ACITP'
admin.site.site_title = 'Admin ACITP'
admin.site.index_title = 'Gestão da Casa do Idoso para Todos os Povos'
