from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategoriaView, \
        SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, \
        MarcaView, MarcaNew, MarcaEdit, MarcaInactivar, \
        UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, UnidadMedidaInactivar, \
        ProductoView, ProductoNew, ProductoEdit, ProductoInactivar

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

    path('unidadesmedida/', UnidadMedidaView.as_view(), name="unidad_medida_list"),
    path('unidadesmedidas/new', UnidadMedidaNew.as_view(), name="unidad_medida_new"),
    path('unidadesmedidas/edit/<int:pk>', UnidadMedidaEdit.as_view(), name="unidad_medida_edit"),
    path('unidadesmedidas/inactivar/<int:id>', UnidadMedidaInactivar, name="unidad_medida_inactivar"),

    path('producto/', ProductoView.as_view(), name="producto_list"),
    path('producto/new', ProductoNew.as_view(), name="producto_new"),
    path('producto/edit/<int:pk>', ProductoEdit.as_view(), name="producto_edit"),
    path('producto/inactivar/<int:id>', ProductoInactivar, name="producto_inactivar"),

]