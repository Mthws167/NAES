from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate
from .views import AdministradorCreate, AdministradorUpdate


urlpatterns = [
    ## URL CREATE
    path("cadastrar/empresa/", EmpresaCreate.as_view(), name="cadastrar-empresa"),
    path("cadastrar/administrador/", AdministradorCreate.as_view(), name="cadastrar-administrador"),

    ## URL UPDATE
    path("editar/empresa/<int:pk>/", EmpresaUpdate.as_view(), name="editar-empresa"),
    path("editar/administrador/<int:pk>/", AdministradorUpdate.as_view(),name="editar-administrador"),

]
