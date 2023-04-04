from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate
from .views import AdministradorCreate, AdministradorUpdate
from .views import ClienteCreate, ClienteUpdate
from .views import MarcaCreate, MarcaUpdate
from .views import ModeloCreate, ModeloUpdate
from .views import MotoCreate, ModeloUpdate
from .views import VendaCreate, VendaUpdate


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
    path("cadastrar/cliente/<int:pk>/",ClienteCreate.as_view(), name="editar-cliente"),
    path("cadastrar/marca/<int:pk>/",MarcaCreate.as_view(), name="editar-marca"),
    path("cadastrar/modelo/<int:pk>/",ModeloCreate.as_view(), name="editar-modelo"),
    path("cadastrar/moto/<int:pk>/",MotoCreate.as_view(), name="editar-moto"),
    path("cadastrar/venda/<int:pk>/",VendaCreate.as_view(), name="editar-venda"),
]
