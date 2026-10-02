from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .models import Producto, Categoria


def inicio(request):
    # Consulta usando el ORM de Django con optimización de llaves foráneas
    productos = Producto.objects.select_related('categoria').all().order_by('id_producto')
    categorias = Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'principal/inicio.html', context)


@login_required
def dashboard_view(request):
    productos = Producto.objects.select_related('categoria').all()
    total_productos = productos.count()
    return render(request, 'principal/dashboard.html', {
        'productos': productos,
        'total_productos': total_productos,
    })


def logout_view(request):
    logout(request)
    return redirect('inicio')