from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, MarcaView, MarcaNew, MarcaEdit, MarcaInactivar

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name="categoria_list"),
    path('categoria/new', CategoriaNew.as_view(), name="categoria_new"),
    path('categoria/edit/<int:pk>', CategoriaEdit.as_view(), name="categoria_edit"),
    path('categoria/delete/<int:pk>', CategoriaDel.as_view(), name="categoria_del"),
    
    path('subcategorias/', SubCategoriaView.as_view(), name="subcategoria_list"),
    path('subcategoria/new', SubCategoriaNew.as_view(), name="subcategoria_new"),
    path('subcategoria/edit/<int:pk>', SubCategoriaEdit.as_view(), name="subcategoria_edit"),
    path('subcategoria/delete/<int:pk>', SubCategoriaDel.as_view(), name="subcategoria_del"),    

    path('marcas/', MarcaView.as_view(), name="marca_list"),
    path('marcas/new', MarcaNew.as_view(), name="marca_new"),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name="marca_edit"),
    path('marcas/inactivar/<int:id>', MarcaInactivar, name="marca_inactivar"),


]