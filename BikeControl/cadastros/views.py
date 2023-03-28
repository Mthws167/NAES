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
    fields = ['nome', 'email', 'telefone']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


#######################################     UPDATE   ######################################################
class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


class AdministradorUpdate(UpdateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('pagina-inicial')


#######################################     DELETE   ######################################################
