from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import CadastroUsuarioForm, DoacaoForm, LoginForm, VoluntarioForm
from .models import Depoimento, EventoCampanha, Instituicao, PrestacaoConta


DEFAULT_EVENTOS = [
    {
        'titulo': 'Festival da Primavera',
        'descricao': 'Festa com musica, danca e atividades ao ar livre para os idosos e suas familias.',
        'data_inicio': timezone.datetime(2026, 3, 15, 14, tzinfo=timezone.get_current_timezone()),
        'data_fim': timezone.datetime(2026, 3, 15, 18, tzinfo=timezone.get_current_timezone()),
        'local': 'Sede Principal',
    },
    {
        'titulo': 'Bazar Solidario',
        'descricao': 'Bazar beneficente com roupas, artesanato e comidas tipicas.',
        'data_inicio': timezone.datetime(2026, 4, 22, 9, tzinfo=timezone.get_current_timezone()),
        'data_fim': timezone.datetime(2026, 4, 22, 17, tzinfo=timezone.get_current_timezone()),
        'local': 'Praca Central',
    },
]

DEFAULT_DEPOIMENTOS = [
    {
        'nome': 'Dona Maria, 78 anos',
        'texto': 'Aqui encontrei uma nova familia. As atividades me dao alegria de viver e os voluntarios sao anjos na minha vida.',
    },
    {
        'nome': 'Luciana Silva',
        'texto': 'Desde que meu pai chegou ao Lar, sinto uma paz imensa. O carinho e a atencao que ele recebe sao visiveis em seu sorriso diario.',
    },
    {
        'nome': 'Ricardo Oliveira',
        'texto': 'O atendimento medico e as atividades recreativas superaram todas as nossas expectativas.',
    },
]


def get_instituicao():
    return Instituicao.objects.first() or Instituicao()


def get_eventos():
    eventos = list(EventoCampanha.objects.filter(ativo=True)[:6])
    return eventos or DEFAULT_EVENTOS


def get_depoimentos():
    depoimentos = list(Depoimento.objects.filter(ativo=True)[:6])
    return depoimentos or DEFAULT_DEPOIMENTOS


def home(request):
    return render(request, 'core/home.html', {
        'instituicao': get_instituicao(),
        'eventos': get_eventos()[:2],
        'depoimentos': get_depoimentos()[:3],
    })


def historia(request):
    return render(request, 'core/historia.html', {'instituicao': get_instituicao()})


def eventos(request):
    return render(request, 'core/eventos.html', {
        'instituicao': get_instituicao(),
        'eventos': get_eventos(),
    })


def doacoes(request):
    form = DoacaoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        doacao = form.save(commit=False)
        if request.user.is_authenticated:
            doacao.registrado_por = request.user
        doacao.save()
        messages.success(request, 'Doacao registrada com sucesso. Obrigado pelo apoio!')
        return redirect('doacoes')

    return render(request, 'core/doacao.html', {
        'instituicao': get_instituicao(),
        'form': form,
    })


def voluntariado(request):
    form = VoluntarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Inscricao enviada com sucesso. Em breve entraremos em contato!')
        return redirect('voluntariado')

    return render(request, 'core/voluntario.html', {
        'instituicao': get_instituicao(),
        'form': form,
    })


def depoimentos(request):
    return render(request, 'core/depoimentos.html', {
        'instituicao': get_instituicao(),
        'depoimentos': get_depoimentos(),
    })


def transparencia(request):
    prestacoes = PrestacaoConta.objects.filter(publicado=True)
    return render(request, 'core/transparencia.html', {
        'instituicao': get_instituicao(),
        'prestacoes': prestacoes,
    })


def cadastro(request):
    form = CadastroUsuarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Conta criada com sucesso.')
        return redirect('home')
    return render(request, 'core/cadastro.html', {'form': form})


def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login_id = form.cleaned_data['username']
        username = login_id
        if '@' in login_id:
            username = User.objects.filter(email__iexact=login_id).values_list('username', flat=True).first() or login_id
        user = authenticate(
            request,
            username=username,
            password=form.cleaned_data['password'],
        )
        if user is not None:
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect('/admin/')
            return redirect('home')
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
