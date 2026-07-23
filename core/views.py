from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import CadastroUsuarioForm, DoacaoForm, LoginForm, VoluntarioForm
from .models import Testimonial, Event, Instituicao, PrestacaoConta, SiteConfiguration



def get_site_config():
    return SiteConfiguration.objects.first() or SiteConfiguration()

def common_context():
    return {"site_config": get_site_config()}


def get_instituicao():
    return Instituicao.objects.first() or Instituicao()


def events_page(request):
    context = {
        **common_context(),
        "events": Event.objects.filter(is_active=True),
    }
    return render(request, "core/events.html", context)


def testimonials_page(request):
    return render(request, "core/testimonials.html", {
        **common_context(),
        "testimonials": Testimonial.objects.filter(is_active=True),
    })

def home(request):
    return render(request, 'core/home.html', {
        **common_context(),
        'instituicao': get_instituicao(),
        'eventos': Event.objects.filter(is_active=True)[:2],
        'testimonials': Testimonial.objects.filter(
            is_active=True,
            is_featured=True,
        )[:3],
    })


def historia(request):
    return render(request, 'core/historia.html', {'instituicao': get_instituicao()})


def eventos(request):
    return render(request, 'core/eventos.html', {
        **common_context(),
        'instituicao': get_instituicao(),
        'eventos': Event.objects.filter(is_active=True),
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
