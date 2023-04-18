from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate, EmpresaDelete,EmpresaList
from .views import AdministradorCreate, AdministradorUpdate, AdministradorDelete,AdministradorList
from .views import ClienteCreate, ClienteUpdate , ClienteDelete,ClienteList
from .views import MarcaCreate, MarcaUpdate, MarcaDelete,MarcaList
from .views import ModeloCreate, ModeloUpdate, ModeloDelete,ModeloList
from .views import MotoCreate, MotoUpdate, MotoDelete,MotoList
from .views import VendaCreate, VendaUpdate, VendaDelete,VendaList


urlpatterns = [
    ## URL CREATE
    path("cadastrar/empresa/", EmpresaCreate.as_view(), name="cadastrar-empresa"),
    path("cadastrar/administrador/", AdministradorCreate.as_view(), name="cadastrar-administrador"),
    path("cadastrar/cliente/", ClienteCreate.as_view(), name="cadastrar-cliente"),
    path("cadastrar/marca/", MarcaCreate.as_view(), name="cadastrar-marca"),
    path("cadastrar/modelo/", ModeloCreate.as_view(), name="cadastrar-modelo"),
    path("cadastrar/moto/", MotoCreate.as_view(), name="cadastrar-moto"),
    path("cadastrar/venda/", VendaCreate.as_view(), name="cadastrar-venda"),

    ## URL UPDATE
    path("editar/empresa/<int:pk>/",EmpresaUpdate.as_view(), name="editar-empresa"),
    path("editar/administrador/<int:pk>/",AdministradorUpdate.as_view(),name="editar-administrador"),
    path("editar/cliente/<int:pk>/",ClienteUpdate.as_view(), name="editar-cliente"),
    path("editar/marca/<int:pk>/",MarcaUpdate.as_view(), name="editar-marca"),
    path("editar/modelo/<int:pk>/",ModeloUpdate.as_view(), name="editar-modelo"),
    path("editar/moto/<int:pk>/",MotoUpdate.as_view(), name="editar-moto"),
    path("editar/venda/<int:pk>/",VendaUpdate.as_view(), name="editar-venda"),

    ## URL DELETE
    path("excluir/empresa/<int:pk>/",EmpresaDelete.as_view(), name="editar-empresa"),
    path("excluir/administrador/<int:pk>/",AdministradorDelete.as_view(),name="editar-administrador"),
    path("excluir/cliente/<int:pk>/",ClienteDelete.as_view(), name="editar-cliente"),
    path("excluir/marca/<int:pk>/",MarcaDelete.as_view(), name="editar-marca"),
    path("excluir/modelo/<int:pk>/",ModeloDelete.as_view(), name="editar-modelo"),
    path("excluir/moto/<int:pk>/",MotoDelete.as_view(), name="editar-moto"),
    path("excluir/venda/<int:pk>/",VendaDelete.as_view(), name="editar-venda"),

    ## URL LIST
    path("listar/empresa/", EmpresaList.as_view(), name="listar-empresa"),
    path("listar/administrador/", AdministradorList.as_view(), name="listar-administrador"),
    path("listar/cliente/", ClienteList.as_view(), name="listar-cliente"),
    path("listar/marca/", MarcaList.as_view(), name="listar-marca"),
    path("listar/modelo/", ModeloList.as_view(), name="listar-modelo"),
    path("listar/moto/", MotoList.as_view(), name="listar-moto"),
    path("listar/venda/", VendaList.as_view(), name="listar-venda"),

    # URL DETAIL
    # path("detalhar/empresa/<int:pk>/",EmpresaDetail.as_view(), name="detalhar-empresa"),
    # path("detalhar/administrador/<int:pk>/",AdministradorDetail.as_view(),name="detalhar-administrador"),
    # path("detalhar/cliente/<int:pk>/",ClienteDetail.as_view(), name="detalhar-cliente"),
    # path("detalhar/marca/<int:pk>/",MarcaDetail.as_view(), name="detalhar-marca"),
    # path("detalhar/modelo/<int:pk>/",ModeloDetail.as_view(), name="detalhar-modelo"),
    # path("detalhar/moto/<int:pk>/",MotoDetail.as_view(), name="detalhar-moto"),
    # path("detalhar/venda/<int:pk>/",VendaDetail.as_view(), name="detalhar-venda"),
]
