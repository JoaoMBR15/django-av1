from django import forms
from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'autor',
            'ano',
            'tipo_acervo',
            'categoria',
            'disponivel',
        ]

        labels = {
            'titulo': 'Nome do livro',
            'autor': 'Autor',
            'ano': 'Ano',
            'tipo_acervo': 'Tipo de acervo',
            'categoria': 'Categoria',
            'disponivel': 'Disponível',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do livro'
            }),

            'autor': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do autor'
            }),

            'ano': forms.NumberInput(attrs={
                'placeholder': 'Ex: 2026'
            }),
        }