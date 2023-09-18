from typing import Any
from django.db.models.query import QuerySet
from .models import Empresa, Administrador, Cliente, Marca, Modelo, Moto, Venda, Carrinho, MotoVenda

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal

from dal import autocomplete


# Create your views here.
#######################################     CREATE   ######################################################
class EmpresaCreate(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-empresa')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        return url


class AdministradorCreate(LoginRequiredMixin, CreateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-administrador')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        return url


class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'cep','cidade','uf','logradouro','bairro', 'numero','documento', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        return url


class MarcaCreate(LoginRequiredMixin, CreateView):
    model = Marca
    fields = ['nome', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-marca')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        return url


class ModeloCreate(LoginRequiredMixin, CreateView):
    model = Modelo
    fields = ['nome', 'marca']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelo')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        return url


class MotoCreate(LoginRequiredMixin, CreateView):
    model = Moto

    fields = ['modelo', 'quantidade', 'preco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-moto')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        return url


class VendaCreate(LoginRequiredMixin, CreateView):
    model = Venda
    fields = ['empresa', 'cliente']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        prod_carrinho = Carrinho.objects.all()

        valor_total = 0.0

        for c in prod_carrinho:

            moto = c.moto

            valor_total += float(moto.preco) * c.quantidade

            MotoVenda.objects.create(
                venda=self.object,
                moto=moto,
                preco=moto.preco * c.quantidade,
                quantidade=c.quantidade
            )

            # Atualiza apenas as motos no carrinho
            moto.quantidade -= c.quantidade
            moto.save()

            c.delete()

        # Atualiza o objedo da venda com o valor total novo
        self.object.valor = valor_total
        # Faz o UPDATE no banco de dados
        self.object.save()

        return url


class CarrinhoCreate(LoginRequiredMixin, CreateView):
    model = Carrinho
    fields = ['moto', 'quantidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-carrinho')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user

        url = super().form_valid(form)

        return url

#######################################     UPDATE   ######################################################


class EmpresaUpdate(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = ['nome', 'email', 'telefone', 'documento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-empresa')


class AdministradorUpdate(LoginRequiredMixin, UpdateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-administrador')


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone',
              'dataNascimento', 'documento', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')


class MarcaUpdate(LoginRequiredMixin, UpdateView):
    model = Marca
    fields = ['nome', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-marca')


class ModeloUpdate(LoginRequiredMixin, UpdateView):
    model = Modelo
    fields = ['nome', 'marca']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modelo')


class MotoUpdate(LoginRequiredMixin, UpdateView):
    model = Moto
    fields = ['modelo', 'quantidade', 'preco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-moto')


class VendaUpdate(LoginRequiredMixin, UpdateView):
    model = Venda
    fields = ['empresa', 'cliente', 'moto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')


class CarrinhoUpdate(LoginRequiredMixin, UpdateView):
    model = Carrinho
    fields = ['moto', 'quantidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-carrinho')

#######################################     DELETE   ######################################################


class EmpresaDelete(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy('listar-empresa')


class AdministradorDelete(LoginRequiredMixin, DeleteView):
    model = Administrador
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy('listar-administrador')


class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-cliente')


class MarcaDelete(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-marca')


class ModeloDelete(LoginRequiredMixin, DeleteView):
    model = Modelo
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-modelo')


class MotoDelete(LoginRequiredMixin, DeleteView):
    model = Moto
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-moto')


class VendaDelete(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-venda')


class CarrinhoDelete(LoginRequiredMixin, DeleteView):
    model = Carrinho
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-carrinho')

#######################################     LIST   ######################################################


class EmpresaList(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = "cadastros/empresa_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Empresa.objects.filter(cadastrado_por=self.request.user).select_related('administrador')


class AdministradorList(LoginRequiredMixin, ListView):
    model = Administrador
    template_name = "cadastros/administrador_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Administrador.objects.filter(usuario=self.request.user)


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cadastros/cliente_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Cliente.objects.filter(cadastrado_por=self.request.user)


class MarcaList(LoginRequiredMixin, ListView):
    model = Marca
    template_name = "cadastros/marca_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Marca.objects.filter(cadastrado_por=self.request.user)


class ModeloList(LoginRequiredMixin, ListView):
    model = Modelo
    template_name = "cadastros/modelo_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Modelo.objects.filter(cadastrado_por=self.request.user).select_related('marca')


class MotoList(ListView):
    model = Moto
    template_name = "cadastros/moto_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Moto.objects.filter(cadastrado_por=self.request.user).select_related('modelo','modelo__marca')


class VendaList(LoginRequiredMixin, ListView):
    model = Venda
    template_name = "cadastros/venda_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Venda.objects.filter(cadastrado_por=self.request.user).select_related('empresa','cliente')


class CarrinhoList(LoginRequiredMixin, ListView):
    model = Carrinho
    template_name = "cadastros/carrinho_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Carrinho.objects.filter(cadastrado_por=self.request.user).select_related('moto')

############################ DETALHES ###########################



