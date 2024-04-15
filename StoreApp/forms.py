from django import forms 
from StoreApp.models import Cliente

#Criando um formulário baseado num model
class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cliente 
        fields = '__all__'
