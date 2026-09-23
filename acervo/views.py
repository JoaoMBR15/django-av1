from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Livro
from .forms import LivroForm


def inicio(request):
    return HttpResponse('Olá, acervo')


def lista_livros(request):

    livros = Livro.objects.all()

    # Pesquisa por nome
    nome = request.GET.get('nome', '')

    # Filtro por tipo
    tipo = request.GET.get('tipo', '')

    # Filtro por categoria
    categoria = request.GET.get('categoria', '')

    if nome:
        livros = livros.filter(titulo__icontains=nome)

    if tipo:
        livros = livros.filter(tipo_acervo=tipo)

    if categoria:
        livros = livros.filter(categoria=categoria)

    return render(
        request,
        'acervo/lista.html',
        {
            'livros': livros,
            'nome': nome,
            'tipo': tipo,
            'categoria': categoria,
        }
    )


def novo_livro(request):

    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista')

    else:
        form = LivroForm()

    return render(
        request,
        'acervo/form.html',
        {'form': form}
    )