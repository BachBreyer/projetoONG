from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Doacao, MensagemContato, Voluntario


class CadastroUsuarioForm(forms.Form):
    nome = forms.CharField(max_length=150)
    telefone = forms.CharField(max_length=30, required=False)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Ja existe uma conta com este e-mail.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'As senhas nao conferem.')
        return cleaned_data

    def save(self):
        email = self.cleaned_data['email'].lower()
        user = User.objects.create_user(
            username=email,
            email=email,
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['nome'],
        )
        Voluntario.objects.get_or_create(
            email=user.email,
            defaults={
                'nome': self.cleaned_data['nome'],
                'telefone': self.cleaned_data.get('telefone', ''),
            },
        )
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='E-mail ou usuario')


class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome', 'email', 'telefone', 'profissao', 'motivacao']


class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['doador_nome', 'doador_email', 'doador_telefone', 'tipo', 'descricao', 'valor', 'item_doado', 'quantidade']


class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'telefone', 'assunto', 'mensagem']
