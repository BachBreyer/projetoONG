from django.conf import settings
from django.db import models
from django.utils import timezone


class Instituicao(models.Model):
    nome = models.CharField(max_length=150, default='ACITP')
    descricao = models.TextField(blank=True)
    historia = models.TextField(blank=True)
    endereco = models.CharField(max_length=255, default='Estrada do Babi, 14455, Vila Magalhaes em Belford Roxo')
    telefone = models.CharField(max_length=30, default='(+55) 21 96441-4945')
    email = models.EmailField(default='acitp2010@gmail.com')
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    chave_pix = models.CharField(max_length=120, default='acitp2010@gmail.com')
    formas_doacao = models.TextField(blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'instituicao'
        verbose_name_plural = 'instituicoes'

    def __str__(self):
        return self.nome

class OrderedContent(models.Model):
    order = models.PositiveIntegerField(default=0, verbose_name="Ordem")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("order", "id")


class Voluntario(models.Model):
    STATUS_NOVO = 'novo'
    STATUS_EM_ANALISE = 'em_analise'
    STATUS_APROVADO = 'aprovado'
    STATUS_INATIVO = 'inativo'
    STATUS_CHOICES = [
        (STATUS_NOVO, 'Novo'),
        (STATUS_EM_ANALISE, 'Em analise'),
        (STATUS_APROVADO, 'Aprovado'),
        (STATUS_INATIVO, 'Inativo'),
    ]

    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=30)
    profissao = models.CharField(max_length=120, blank=True)
    motivacao = models.TextField(blank=True)
    disponibilidade = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NOVO)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'voluntario'
        verbose_name_plural = 'voluntarios'

    def __str__(self):
        return self.nome


class Doacao(models.Model):
    TIPO_DINHEIRO = 'dinheiro'
    TIPO_ITEM = 'item'
    TIPO_ALIMENTO = 'alimento'
    TIPO_MEDICAMENTO = 'medicamento'
    TIPO_OUTRO = 'outro'
    TIPO_CHOICES = [
        (TIPO_DINHEIRO, 'Dinheiro'),
        (TIPO_ITEM, 'Item'),
        (TIPO_ALIMENTO, 'Alimento'),
        (TIPO_MEDICAMENTO, 'Medicamento'),
        (TIPO_OUTRO, 'Outro'),
    ]

    doador_nome = models.CharField(max_length=150, blank=True)
    doador_email = models.EmailField(blank=True)
    doador_telefone = models.CharField(max_length=30, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default=TIPO_DINHEIRO)
    data = models.DateField(default=timezone.now)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    item_doado = models.CharField(max_length=150, blank=True)
    quantidade = models.CharField(max_length=50, blank=True)
    registrado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data', '-criado_em']
        verbose_name = 'doacao'
        verbose_name_plural = 'doacoes'

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.data:%d/%m/%Y}'


class EventoCampanha(models.Model):
    CATEGORIA_EVENTO = 'evento'
    CATEGORIA_CAMPANHA = 'campanha'
    CATEGORIA_ACAO = 'acao_social'
    CATEGORIA_CHOICES = [
        (CATEGORIA_EVENTO, 'Evento'),
        (CATEGORIA_CAMPANHA, 'Campanha'),
        (CATEGORIA_ACAO, 'Acao social'),
    ]

    titulo = models.CharField(max_length=150)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default=CATEGORIA_EVENTO)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)
    local = models.CharField(max_length=180, blank=True)
    imagem = models.ImageField(upload_to='eventos/', blank=True)
    meta_arrecadacao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_inicio']
        verbose_name = 'evento ou campanha'
        verbose_name_plural = 'eventos e campanhas'

    def __str__(self):
        return self.titulo


class Testimonial(OrderedContent):
    author_name = models.CharField(max_length=120)
    author_role = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    is_featured = models.BooleanField(default=True, verbose_name="Destacar na home")

    class Meta(OrderedContent.Meta):
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return self.author_name


class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=30, blank=True)
    assunto = models.CharField(max_length=150)
    mensagem = models.TextField()
    respondida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criada_em']
        verbose_name = 'mensagem de contato'
        verbose_name_plural = 'mensagens de contato'

    def __str__(self):
        return f'{self.nome} - {self.assunto}'


class PrestacaoConta(models.Model):
    titulo = models.CharField(max_length=150)
    periodo_inicio = models.DateField()
    periodo_fim = models.DateField()
    resumo = models.TextField()
    valor_arrecadado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_utilizado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    arquivo = models.FileField(upload_to='prestacoes/', blank=True)
    publicado = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-periodo_fim']
        verbose_name = 'prestacao de conta'
        verbose_name_plural = 'prestacoes de contas'

    def __str__(self):
        return self.titulo

class SiteConfiguration(models.Model):
    organization_name = models.CharField(max_length=120, default="ACITP")
    hero_badge = models.CharField(
        max_length=180,
        default="ONG ACITP - A CASA DO IDOSO PARA TODOS OS POVOS",
    )
    hero_title = models.CharField(
        max_length=180,
        default="Cuidando de quem sempre cuidou de nos",
    )
    hero_description = models.TextField(
        default=(
            "Ha 15 anos levando dignidade, amor e qualidade de vida para idosos "
            "em situacao de vulnerabilidade."
        )
    )
    history_title = models.CharField(
        max_length=180,
        default="Uma decada de amor e dedicacao",
    )
    history_description = models.TextField(
        default=(
            "Fundada em 2010, a ACITP nasceu para acolher idosos em "
            "vulnerabilidade com dignidade, cuidado e presenca diaria."
        )
    )
    history_highlight = models.CharField(max_length=140, default="Nossa Historia")
    director_role = models.CharField(max_length=120, default="Diretor e Fundador")
    director_name = models.CharField(max_length=120, default="Pastor Marcio Vieira")
    services_title = models.CharField(max_length=140, default="Nossos Servicos")
    services_description = models.TextField(
        default="Oferecemos um cuidado integral, atendendo as necessidades fisicas, emocionais e sociais dos nossos idosos."
    )
    donation_title = models.CharField(max_length=140, default="Apoie Nossa Causa")
    donation_description = models.TextField(
        default="Sua contribuicao ajuda na alimentacao, nos medicamentos, nos eventos e na manutencao da instituicao."
    )
    pix_key = models.CharField(max_length=180, default="acitp2010@gmail.com")
    volunteer_title = models.CharField(max_length=140, default="Seja Voluntario")
    volunteer_intro = models.TextField(
        default="Doe seu tempo e suas habilidades. Precisamos de pessoas dispostas a fazer companhia, apoiar e cuidar."
    )
    volunteer_benefits = models.TextField(
        default=(
            "Atividades recreativas e culturais\n"
            "Acompanhamento em consultas medicas\n"
            "Apoio administrativo e logistico\n"
            "Oficinas de artesanato e musica"
        )
    )
    contact_phone = models.CharField(max_length=40, default="(+55) 21 96441-4945")
    contact_email = models.EmailField(default="acitp2010@gmail.com")
    contact_address = models.TextField(
        default="Estrada do Babi, 14455, Vila Magalhaes em Belford Roxo"
    )
    footer_text = models.TextField(
        default="Transformando vidas com amor e dignidade desde 2010. Cada idoso merece ser cuidado com carinho."
    )
    hero_image = models.FileField(upload_to="site/", blank=True, null=True)
    events_banner = models.FileField(upload_to="site/", blank=True, null=True)

    class Meta:
        verbose_name = "Configuracao do site"
        verbose_name_plural = "Configuracao do site"

    def __str__(self):
        return f"Configuracao - {self.organization_name}"

    @property
    def volunteer_benefits_list(self):
        return [item.strip() for item in self.volunteer_benefits.splitlines() if item.strip()]
