from typing import Any, Dict
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy

class UsuarioCreate(CreateView):
    template_name="cadastros/form.html"
    form_class = UsuarioForm
    success_url= reverse_lazy('login')

# Create your views here.
    def get_context_data(self, *args,**kwargs) :
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] =' Registro novo Usuário'

        return context