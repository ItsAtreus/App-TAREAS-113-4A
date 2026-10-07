from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Componente") 
    descripcion = models.TextField(verbose_name="Descripcion tecnica")
    # Validamos que el precio sea mayor a 0 y el stock no sea negativo
    precio = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Precio ($)")
    stock = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Stock disponible")
    categoria = models.CharField(max_length=100, verbose_name="Categoria (Ej: GPU, RAM, Placa Madre)")

    def __str__(self):
        return self.nombre