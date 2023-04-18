from .models import Empresa,Administrador,Cliente,Marca,Modelo,Moto,Venda

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
#######################################     CREATE   ######################################################
class EmpresaCreate(LoginRequiredMixin ,CreateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

class AdministradorCreate(LoginRequiredMixin ,CreateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone','dataNascimento', 'documento','senha']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

class ClienteCreate(LoginRequiredMixin ,CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

class MarcaCreate(LoginRequiredMixin ,CreateView):
    model = Marca
    fields = ['nome', 'pais', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')   

class ModeloCreate(LoginRequiredMixin ,CreateView):
    model = Modelo
    fields = ['nome', 'marca', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

class MotoCreate(LoginRequiredMixin ,CreateView):
    model = Moto
    fields = ['modelo', 'quantidade', 'preco', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

class VendaCreate(LoginRequiredMixin ,CreateView):
    model = Venda
    fields = ['empresa', 'cliente','moto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial') 


#######################################     UPDATE   ######################################################
class EmpresaUpdate(LoginRequiredMixin ,UpdateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Empresa"
        return dados


class AdministradorUpdate(LoginRequiredMixin ,UpdateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Administrador"
        return dados


class ClienteUpdate(LoginRequiredMixin ,UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Cliente"
        return dados


class MarcaUpdate(LoginRequiredMixin ,UpdateView):
    model = Marca
    fields = ['nome', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Marca"
        return dados


class ModeloUpdate(LoginRequiredMixin ,UpdateView):
    model = Modelo
    fields = ['nome', 'marca']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Modelo"
        return dados


class MotoUpdate(LoginRequiredMixin ,UpdateView):
    model = Moto
    fields = ['modelo', 'datafabricacao', 'quantidade', 'preco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Moto"
        return dados


class VendaUpdate(LoginRequiredMixin ,UpdateView):
    model = Venda
    fields = ['empresa', 'cliente', 'moto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    def get_context_data(self, *args,**kwargs):
        dados = super().get_context_data(*args,**kwargs)
        dados["titulo"]="Atualizar Venda"
        return dados


#######################################     DELETE   ######################################################
class EmpresaDelete(LoginRequiredMixin ,DeleteView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


class AdministradorDelete(LoginRequiredMixin ,DeleteView):
    model = Administrador
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


class ClienteDelete(LoginRequiredMixin ,DeleteView):
    model = Cliente
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class MarcaDelete(LoginRequiredMixin ,DeleteView):
    model = Marca
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class ModeloDelete(LoginRequiredMixin ,DeleteView):
    model = Modelo
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class MotoDelete(LoginRequiredMixin ,DeleteView):
    model = Moto
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')


class VendaDelete(LoginRequiredMixin ,DeleteView):
    model = Venda
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagina-inicial')

    
#######################################     LIST   ######################################################
class EmpresaList(LoginRequiredMixin ,ListView):
    model = Empresa
    template_name = "cadastros/empresa_list.html"


class AdministradorList(LoginRequiredMixin ,ListView):
    model = Administrador
    template_name = "cadastros/administrador_list.html"


class ClienteList(LoginRequiredMixin ,ListView):
    model = Cliente
    template_name = "cadastros/cliente_list.html"


class MarcaList(LoginRequiredMixin ,ListView):
    model = Marca
    template_name = "cadastros/marca_list.html"


class ModeloList(LoginRequiredMixin ,ListView):
    model = Modelo
    template_name = "cadastros/modelo_list.html"


class MotoList(LoginRequiredMixin ,ListView):
    model = Moto
    template_name = "cadastros/moto_list.html"


class VendaList(LoginRequiredMixin ,ListView):
    model = Venda
    template_name = "cadastros/venda_list.html"



#######################################     DETAIL   ######################################################
