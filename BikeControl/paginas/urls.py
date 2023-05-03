from django.urls import path
from .views import IndexView

urlpatterns = [

    path("", IndexView.as_view(), name="index"),
    path("sobre/",views.LoginView.as_view(template_name="paginas/sobre.html",name="sobre"),


]
