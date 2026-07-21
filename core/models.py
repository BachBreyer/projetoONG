from django.db import models

class Depoimento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Autor")
    cargo_ou_relacao = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cargo ou Relação")
    texto = models.TextField(verbose_name="Depoimento")
    foto = models.ImageField(upload_to='depoimentos/', blank=True, null=True, verbose_name="Foto")
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.nome} - {self.cargo_ou_relacao or 'Voluntário'}"


class Evento(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título do Evento")
    descricao = models.TextField(verbose_name="Descrição")
    data_inicio = models.DateTimeField(verbose_name="Data e Hora de Início")
    local = models.CharField(max_length=200, verbose_name="Local")
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True, verbose_name="Imagem de Capa")
    ativo = models.BooleanField(default=True, verbose_name="Evento Ativo?")
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['data_inicio']

    def __str__(self):
        return self.titulo
