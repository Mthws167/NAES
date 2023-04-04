from .models import Empresa,Administrador,Cliente,Marca,Modelo,Moto,Venda

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
#######################################     CREATE   ######################################################
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


class AdministradorCreate(CreateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone','dataNascimento', 'documento','senha']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

class MarcaCreate(CreateView):
    model = Marca
    fields = ['nome', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')    

class ModeloCreate(CreateView):
    model = Modelo
    fields = ['nome', 'marca']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class MotoCreate(CreateView):
    model = Moto
    fields = ['modelo', 'datafabricacao','quantidade','preco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

class VendaCreate(CreateView):
    model = Venda
    fields = ['empresa', 'cliente','moto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial') 


#######################################     UPDATE   ######################################################
class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


class AdministradorUpdate(UpdateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class MarcaUpdate(UpdateView):
    model = Marca
    fields = ['nome', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class ModeloUpdate(UpdateView):
    model = Modelo
    fields = ['nome', 'marca']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class MotoUpdate(UpdateView):
    model = Moto
    fields = ['modelo', 'datafabricacao', 'quantidade', 'preco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class VendaUpdate(UpdateView):
    model = Venda
    fields = ['empresa', 'cliente', 'moto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


#######################################     DELETE   ######################################################
