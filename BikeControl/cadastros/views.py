from .models import Empresa,Administrador,Cliente,Marca,Modelo,Moto,Venda

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
#######################################     CREATE   ######################################################
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Cadastro de Empresa"
        return dados


class AdministradorCreate(CreateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone','dataNascimento', 'documento','senha']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Administrador"
        return dados

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Cadastro de Cliente"
        return dados

class MarcaCreate(CreateView):
    model = Marca
    fields = ['nome', 'pais', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')   

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Cadastro de Marca"
        return dados 

class ModeloCreate(CreateView):
    model = Modelo
    fields = ['nome', 'marca', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Cadastro de Modelo"
        return dados


class MotoCreate(CreateView):
    model = Moto
    fields = ['modelo', 'quantidade', 'preco', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Cadastro de Moto"
        return dados

class VendaCreate(CreateView):
    model = Venda
    fields = ['empresa', 'cliente','moto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial') 

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Cadastro de Venda"
        return dados


#######################################     UPDATE   ######################################################
class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Empresa"
        return dados


class AdministradorUpdate(UpdateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Administrador"
        return dados


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Cliente"
        return dados


class MarcaUpdate(UpdateView):
    model = Marca
    fields = ['nome', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Marca"
        return dados


class ModeloUpdate(UpdateView):
    model = Modelo
    fields = ['nome', 'marca']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Modelo"
        return dados


class MotoUpdate(UpdateView):
    model = Moto
    fields = ['modelo', 'datafabricacao', 'quantidade', 'preco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Moto"
        return dados


class VendaUpdate(UpdateView):
    model = Venda
    fields = ['empresa', 'cliente', 'moto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Venda"
        return dados


#######################################     LIST   ######################################################


#######################################     DELETE   ######################################################
class EmpresaDelete(DeleteView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


class AdministradorDelete(DeleteView):
    model = Administrador
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class MarcaDelete(DeleteView):
    model = Marca
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class ModeloDelete(DeleteView):
    model = Modelo
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class MotoDelete(DeleteView):
    model = Moto
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class VendaDelete(DeleteView):
    model = Venda
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')