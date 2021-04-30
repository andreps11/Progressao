# from django.views.generic import TemplateView

from django.views.generic.list import ListView

from cadastros.models import Produto
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class InicioView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = "paginas/inicio.html"

