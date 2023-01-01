from django.urls import path
from .views import AlmacenView, CategoriaView

urlpatterns = [
    path('almacenes/', AlmacenView.as_view(), name='lista_almacenes'),
    path('categorias/', CategoriaView.as_view(), name='lista_categorias')
]