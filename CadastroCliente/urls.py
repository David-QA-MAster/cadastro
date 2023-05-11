from django.urls import path
from CadastroCliente import views 

urlpatterns = [
    path('', views.index, name= 'index' ),
    path('clientes' , views.listar_clientes, name='clientes'),
    path('Profissao' , views.lista_profissao, name='Profissao'),
    path('cliente/<int:id>', views.detalhar_cliente, name= 'detalhar'),
]