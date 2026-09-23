from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
]

from django.urls import path
from . import views
urlpatterns = [
    path(
        'livros/',
        views.lista_livros,
        name='lista'
    ),
]
