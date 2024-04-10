from StoreApp.models import Departamento

def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    
    context = {
        'departamentos' : departamentos
    }
    return context
