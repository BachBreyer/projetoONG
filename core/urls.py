from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('historia/', views.historia, name='historia'),
    path('eventos/', views.eventos, name='eventos'),
    path('doacoes/', views.doacoes, name='doacoes'),
    path('voluntariado/', views.voluntariado, name='voluntariado'),
    path('depoimentos/', views.depoimentos, name='depoimentos'),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
