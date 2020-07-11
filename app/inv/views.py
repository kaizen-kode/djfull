from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm

from bases.views import SinPrivilegios
class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    

class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_Crea = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    
    success_message = "Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_Modifica = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required = "inv.delete_categoria"
    model = Categoria
    template_name = "inv/categoria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")


class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"


class SubCategoriaNew(SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    
    
    def form_valid(self, form):
        form.instance.usuario_Crea = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    
    
    def form_valid(self, form):
        form.instance.usuario_Modifica = self.request.user.id
        return super().form_valid(form)


class SubCategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required = "inv.delete_subcategoria"
    model = SubCategoria
    template_name = "inv/marca_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")


class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"

    
class MarcaNew(SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_marca"
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    
    def form_valid(self, form):
        form.instance.usuario_Crea = self.request.user
        return super().form_valid(form)


class MarcaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_marca"
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    
    def form_valid(self, form):
        form.instance.usuario_Modifica = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='base:sin_privilegios')
def MarcaInactivar(request, id):
    marca = Marca.objects.filter(pk= id).first()
    contexto = {}
    template_name = "inv/marca_del.html"

    if not marca:
        return redirect("inv:marca_list")
    
    if request.method=='GET':
        contexto ={'obj': marca}

    if request.method=='POST':
        marca.estado = False
        marca.save()
        messages.success(request,'Marca Inactivada!.')
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)

#UNIDAD DE MEDIDA
class UnidadMedidaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_unidadmedida"
    model = UnidadMedida
    template_name = "inv/unidad_medida_list.html"
    context_object_name = "obj"
    
class UnidadMedidaNew(SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_unidadmedida"
    model = UnidadMedida
    template_name = "inv/unidad_medida_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidad_medida_list")
    
    def form_valid(self, form):
        form.instance.usuario_Crea = self.request.user
        return super().form_valid(form)


class UnidadMedidaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_unidadmedida"
    model = UnidadMedida
    template_name = "inv/unidad_medida_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:unidad_medida_list")
    
    def form_valid(self, form):
        form.instance.usuario_Modifica = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_unidadmedida', login_url='base:sin_privilegios')
def UnidadMedidaInactivar(request, id):
    unidadmedida = UnidadMedida.objects.filter(pk= id).first()
    contexto = {}
    template_name = "inv/marca_del.html"

    if not unidadmedida:
        return redirect("inv:unidad_medida_list")
    
    if request.method=='GET':
        contexto ={'obj': unidadmedida}

    if request.method=='POST':
        unidadmedida.estado = False
        unidadmedida.save()
        return redirect("inv:unidad_medida_list")

    return render(request, template_name, contexto)


#PRODUCTO
class ProductoView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_producto"
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    
class ProductoNew(SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_unidadmedida"
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    
    def form_valid(self, form):
        form.instance.usuario_Crea = self.request.user
        return super().form_valid(form)


class ProductoEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_unidadmedida"
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    
    def form_valid(self, form):
        form.instance.usuario_Modifica = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_producto', login_url='base:sin_privilegios')
def ProductoInactivar(request, id):
    producto = Producto.objects.filter(pk= id).first()
    contexto = {}
    template_name = "inv/marca_del.html"

    if not producto:
        return redirect("inv:producto_list")
    
    if request.method=='GET':
        contexto ={'obj': producto}

    if request.method=='POST':
        producto.estado = False
        producto.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)
