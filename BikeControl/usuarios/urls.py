from django.urls import path
from django.contrib.auth import views
from .views import UsuarioCreate


urlpatterns = [
    path("login/",views.LoginView.as_view(template_name="cadastros/form.html",extra_context={"titulo": "Autenticação"}),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    path("registrar/", UsuarioCreate.as_view(),name='registrar'),
]
