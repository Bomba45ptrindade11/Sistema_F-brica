from django.urls import path
from .views import listar_produtos, adicionar_produto, atualizar_produto, detalhes_produto, excluir_produto

urlpatterns = [
    path('listar_produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:pk>/', atualizar_produto, name='atualizar_produto'),
    path('produtos/detalhes/<int:pk/',detalhes_produto, name='detalhes_produto'),
    path('produtos/excluir/<int:pk/', excluir_produto, name='excluir_produto'),
]

from .views import custom_login, custom_logout

urlpatterns += [
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]