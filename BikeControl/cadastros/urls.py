from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate, EmpresaDelete,EmpresaList
from .views import AdministradorCreate, AdministradorUpdate, AdministradorDelete,AdministradorList
from .views import ClienteCreate, ClienteUpdate , ClienteDelete,ClienteList
from .views import MarcaCreate, MarcaUpdate, MarcaDelete,MarcaList
from .views import ModeloCreate, ModeloUpdate, ModeloDelete,ModeloList
from .views import MotoCreate, MotoUpdate, MotoDelete,MotoList
#, MotoAutocomplete
from .views import VendaCreate, VendaUpdate, VendaDelete,VendaList
from .views import CarrinhoCreate, CarrinhoUpdate, CarrinhoDelete, CarrinhoList

urlpatterns = [
    ## URL CREATE
    path("cadastrar/empresa/", EmpresaCreate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Cadastrar Empresa"}), name="cadastrar-empresa"),
    path("cadastrar/administrador/", AdministradorCreate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Cadastrar Administrador"}), name="cadastrar-administrador"),
    path("cadastrar/cliente/", ClienteCreate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Cadastrar Cliente"}), name="cadastrar-cliente"),
    path("cadastrar/marca/", MarcaCreate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Cadastrar Marca"}), name="cadastrar-marca"),
    path("cadastrar/modelo/", ModeloCreate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Cadastrar Modelo"}), name="cadastrar-modelo"),
    path("cadastrar/moto/", MotoCreate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Cadastrar Moto"}), name="cadastrar-moto"),
    path("cadastrar/venda/", VendaCreate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Cadastrar Venda"}), name="cadastrar-venda"),
    path("cadastrar/carrinho/", CarrinhoCreate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Cadastrar Carrinho"}), name="cadastrar-carrinho"),

    ## URL UPDATE
    path("editar/empresa/<int:pk>/",EmpresaUpdate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Editar Empresa"}), name="editar-empresa"),
    path("editar/administrador/<int:pk>/",AdministradorUpdate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Editar Administrador"}),name="editar-administrador"),
    path("editar/cliente/<int:pk>/",ClienteUpdate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Editar Cliente"}), name="editar-cliente"),
    path("editar/marca/<int:pk>/",MarcaUpdate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Editar Marca"}), name="editar-marca"),
    path("editar/modelo/<int:pk>/",ModeloUpdate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Editar Modelo"}), name="editar-modelo"),
    path("editar/moto/<int:pk>/",MotoUpdate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Editar Moto"}), name="editar-moto"),
    path("editar/venda/<int:pk>/",VendaUpdate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Editar Venda"}), name="editar-venda"),
    path("editar/carrinho/<int:pk>/",CarrinhoUpdate.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Editar Carrinho"}), name="editar-carrinho"),

    ## URL DELETE
    path("excluir/empresa/<int:pk>/",EmpresaDelete.as_view(template_name="cadastros/form-delete.html",extra_context={"titulo": "Excluir Empresa ?"}), name="excluir-empresa"),
    path("excluir/administrador/<int:pk>/",AdministradorDelete.as_view(template_name="cadastros/form-delete.html",extra_context={"titulo": "Excluir Administrador ?"}),name="excluir-administrador"),
    path("excluir/cliente/<int:pk>/",ClienteDelete.as_view(template_name="cadastros/form-delete.html",extra_context={"titulo": "Excluir Cliente ?"}), name="excluir-cliente"),
    path("excluir/marca/<int:pk>/",MarcaDelete.as_view(template_name="cadastros/form-delete.html",extra_context={"titulo": "Excluir Marca ?"}), name="excluir-marca"),
    path("excluir/modelo/<int:pk>/",ModeloDelete.as_view(template_name="cadastros/form-delete.html",extra_context={"titulo": "Excluir Modelo ?"}), name="excluir-modelo"),
    path("excluir/moto/<int:pk>/",MotoDelete.as_view(template_name="cadastros/form-delete.html",extra_context={"titulo": "Excluir Moto ?"}), name="excluir-moto"),
    path("excluir/venda/<int:pk>/",VendaDelete.as_view(template_name="cadastros/form-delete.html",extra_context={"titulo": "Excluir Venda ?"}), name="excluir-venda"),
    path("excluir/carrinho/<int:pk>/", CarrinhoDelete.as_view(template_name="cadastros/form-delete.html",extra_context={"titulo": "Excluir Carrinho ?"}), name="excluir-carrinho"),
    ## URL LIST
    path("listar/empresa/", EmpresaList.as_view(), name="listar-empresa"),
    path("listar/administrador/", AdministradorList.as_view(), name="listar-administrador"),
    path("listar/cliente/", ClienteList.as_view(), name="listar-cliente"),
    path("listar/marca/", MarcaList.as_view(), name="listar-marca"),
    path("listar/modelo/", ModeloList.as_view(), name="listar-modelo"),
    path("listar/moto/", MotoList.as_view(), name="listar-moto"),
    path("listar/venda/", VendaList.as_view(), name="listar-venda"),
    path("listar/carrinho/", CarrinhoList.as_view(), name="listar-carrinho"),

    # Exemplo de pesquisa com autocomplete
    # path('buscar/moto/', MotoAutocomplete.as_view(), name="busca-moto")
]
