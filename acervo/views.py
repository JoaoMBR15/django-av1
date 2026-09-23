from django.shortcuts import render

from django.http import HttpResponse
def inicio(request):
    return HttpResponse(
        'Olá, acervo'
)

from django.shortcuts import render
from .models import Livro
def lista_livros(request):
    livros = Livro.objects.all() # busca no banco
    return render(
        request, 'acervo/lista.html',
        {'livros': livros} # envia ao template
)