from django.shortcuts import render
from CadastroCliente.models import Cliente, Profissao

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
    lista_profissao = Profissao.objects.all()
    #o dicionário (variavel) context vai mandar pro tamplate 
    context = {
        "cliente": listar_clientes,
        "profissao": lista_profissao
    }

    return render(request, 'lista_clientes.html', context)

def lista_profissao(request):
    lista_profissoes = Profissao.objects.all()
   
    context = {
        "Profissao": lista_profissoes,
    }
    
    return render(request, 'lista_profissoes.html', context)

def detalhar_cliente(request, id):
    cliente = cliente.objects.get(id = id)
    context = {
        "cliente": cliente


    }
    return render(request, "cliente_detalhar.html")