from django.urls import path

from . import views

urlpatterns = [
    path('', views.edit, name="edit"),
    path('lista_questionarios/', views.lista_questionarios, name='lista_questionarios'),
    path('questionario/<int:questionario_id>/', views.detalhes_questionario, name='detalhes_questionario'),
    path('excluir/<int:questionario_id>/', views.excluir_questionario, name='excluir_questionario'),
    path('editar_questionario/<int:questionario_id>/', views.editar_questionario, name='editar_questionario'),
    path('save_edits/<int:questionario_id>/', views.save_edits, name='save_edits'),

]