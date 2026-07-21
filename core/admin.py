from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Depoimento,
    Doacao,
    EventoCampanha,
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


@admin.register(EventoCampanha)
class EventoCampanhaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'data_inicio', 'local', 'preview_imagem', 'ativo']
    list_filter = ['categoria', 'ativo', 'data_inicio']
    search_fields = ['titulo', 'descricao', 'local']

    @admin.display(description='Imagem')
    def preview_imagem(self, obj):
        if not obj.imagem:
            return '-'
        return format_html(
            '<img src="{}" style="width: 72px; height: 52px; object-fit: cover; border-radius: 8px; border: 1px solid #d7ded9;">',
            obj.imagem.url,
        )


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo_ou_relacao', 'ativo', 'criado_em']
    list_filter = ['ativo', 'criado_em']
    search_fields = ['nome', 'texto', 'cargo_ou_relacao']


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
