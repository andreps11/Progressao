from django.urls import path
from .views import ProdutoCreate
from .views import ProdutoUpdate
from .views import ProdutoDelete
from .views import ProdutoList

urlpatterns = [
    path('cadastrar/produto/', ProdutoCreate.as_view(), name="cadastrar-produto"),

    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name="editar-produto"),

    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name="excluir-produto"),

    path('listar/produtos/', ProdutoList.as_view(), name="listar-produto"),
]
