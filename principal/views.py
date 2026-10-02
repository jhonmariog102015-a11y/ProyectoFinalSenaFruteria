from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Producto

def index(request):
    # 2. Traes todos los productos de la base de datos y cuentas el total
    productos = Producto.objects.all()
    total_productos = productos.count()
    
    # 3. Creas un diccionario con los datos para enviarlos al HTML
    context = {
        'productos': productos,
        'total_productos': total_productos,
    }
    
    # 4. Pasas el context como tercer argumento en el render
    return render(request, 'principal/index.html', context)


@login_required
def dashboard_view(request):
    User = get_user_model()
    context = {
        'productos': Producto.objects.all(),
        'total_productos': Producto.objects.count(),
        'total_usuarios': User.objects.count(),
    }
    return render(request, 'principal/dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')