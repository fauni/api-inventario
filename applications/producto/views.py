from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Almacen, Categoria

# Create your views here.

class AlmacenView(View):
    def get(self, request):
        almacenes = list(Almacen.objects.values())
        if len(almacenes) > 0:
            datos = {'message':"Success", 'almacenes': almacenes}
        else:
            datos = {'message': "No existen almacenes ..."}
        return JsonResponse(datos)

class CategoriaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
       
    def get(self, request):
        categorias = list(Categoria.objects.values())
        if len(categorias) > 0:
            datos = {'message':"Success", 'categorias': categorias}
        else:
            datos = {'message': "No existen categorias ..."}
        return JsonResponse(datos)

    def post(self, request):
        print(request.body)
        datos = {'message': "Success"}
        return JsonResponse(datos)

