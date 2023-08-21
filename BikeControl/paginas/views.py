from django.views.generic import TemplateView
from cadastros.models import Venda


class IndexView(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)

        if(self.request.user.is_authenticated):
            # Conte a quantidade de vendas relacionadas ao usuário autenticado
            dados["qtde_vendas"] = Venda.objects.filter(cadastrado_por=self.request.user).count()

        return dados
