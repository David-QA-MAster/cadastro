from django.contrib import admin
from CadastroCliente.models import Cliente,Profissao,Cliente,Telefone,Cliente,Interesse


# Register your models here.
class Telefones(admin.StackedInline):
    model = Telefone
    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cidade') 
    list_display_links = ('id', 'nome')
    list_filter = ('bairro' , 'cidade' , 'ativo')
    inlines = [Telefones] 

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Profissao)
admin.site.register(Telefone)
admin.site.register(Interesse)