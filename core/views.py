from django.shortcuts import render
from .models import Depoimento, Evento

def home(request):
    proximos_eventos = Evento.objects.filter(ativo=True).order_by('data_inicio')[:3]
    depoimentos = Depoimento.objects.all().order_by('-data_criacao')[:3]
    return render(request, 'core/home.html', {
        'eventos': proximos_eventos,
        'depoimentos': depoimentos
    })

def depoimentos_view(request):
    depoimentos = Depoimento.objects.all().order_by('-data_criacao')
    return render(request, 'core/depoimentos.html', {'depoimentos': depoimentos})

def eventos_view(request):
    eventos = Evento.objects.filter(ativo=True).order_by('data_inicio')
    return render(request, 'core/eventos.html', {'eventos': eventos})
