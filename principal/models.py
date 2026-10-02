from django.db import models

# 1.tabla de Categorias

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre              
                
#2 Tabla de productos 
class Producto(models.Model):
    
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
# Relación (Llave Foránea): Un producto pertenece a una categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return f"{self.nombre} - Stock: {self.stock}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre