from django.shortcuts import render
from CadastroCliente.models import Cliente

# Create your views here.

def index(request):
    meu_nome = 'Beltrano da Costa'
    lista_fruta = ['Laranja', 'Maça', 'Banana']
    context = {
        'nome' : meu_nome, 
        'frutas' : lista_fruta
    }
    return render(request, 'index.html', context)

def listar_clientes(request):
    #busca todos os clientes cadastrados na tabela(admin)
    listar_clientes = Cliente.objects.all()
    #o dicionario (variavel) context vai mandar pro tamplate 
    context = {
        "cliente": listar_clientes,
    }

    return render(request, 'lista_clientes.html', context)
