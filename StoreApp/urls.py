from django.urls import path
from StoreApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produto_lista, name='produto_lista'),
    path('produtos/<int:id>', views.produto_lista_por_departamento, name='produto_lista_por_departamento'),   
    path('produto/', views.produto_detalhe, name='produto_detalhe')
   
]