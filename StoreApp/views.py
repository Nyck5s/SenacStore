from django.shortcuts import render
from StoreApp.models import Departamento, Produto

# Create your views here.

def index(request):
    departamentos = Departamento.objects.all()
    
    context = {
        'departamentos' : departamentos
    }
    return render(request, 'index.html', context)

def produto_lista(request):
    produtos_lista = Produto.objects.all()

    context = {
        'produtos' : produtos_lista,
        'titulo' : 'Todos os Produtos'
    }
    return render(request, 'produtos.html', context)

 
def produto_lista_por_departamento(request, id):
    produtos_lista = Produto.objects.filter(departamento_id=id)
    departamento = Departamento.objects.get(id = id)

    context = {
        'produtos' : produtos_lista,
        'titulo' : departamento.nome
    }
    return render(request, 'produtos.html', context)


def produto_detalhe(request):
    return render(request, 'produto_detalhes.html')

