from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Produto
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.


class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Vendedor"
    model = Produto
    fields = ['nome', 'quantidade', 'preco', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

    def form_valid(self, form):

        # Antes do super não foi criado o objeto nem salvo no banco
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro"
        context['botao'] = "Cadastrar"
        # context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Vendedor"
    model = Produto
    fields = ['nome', 'quantidade', 'preco', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Produto, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar"
        context['botao'] = 'Salvar'
        return context



class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Vendedor"
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Produto, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Vendedor"
    model = Produto
    template_name = 'cadastros/listas/produto.html'

    def get_queryset(self):
        self.object_list = Produto.objects.filter(usuario=self.request.user)
        return self.object_list
