from django.test import TestCase
from django.urls import reverse

from .models import Producto


class ProductoCrudTests(TestCase):
    def test_crear_consultar_editar_y_eliminar(self):
        datos = {
            'nombre': 'Memoria RAM',
            'descripcion': '16 GB',
            'precio': 25000,
            'stock': 4,
            'categoria': 'RAM',
        }

        respuesta = self.client.post(reverse('crear_producto'), datos)
        self.assertRedirects(respuesta, reverse('inicio'))
        producto = Producto.objects.get()
        self.assertContains(self.client.get(reverse('inicio')), 'Memoria RAM')
        self.assertContains(
            self.client.get(reverse('detalle_producto', args=[producto.id])),
            '16 GB',
        )

        datos['stock'] = 8
        respuesta = self.client.post(reverse('editar_producto', args=[producto.id]), datos)
        self.assertRedirects(respuesta, reverse('inicio'))
        producto.refresh_from_db()
        self.assertEqual(producto.stock, 8)

        respuesta = self.client.post(reverse('eliminar_producto', args=[producto.id]))
        self.assertRedirects(respuesta, reverse('inicio'))
        self.assertFalse(Producto.objects.exists())

    def test_precio_invalido_no_crea_producto(self):
        respuesta = self.client.post(reverse('crear_producto'), {
            'nombre': 'Memoria RAM',
            'descripcion': '16 GB',
            'precio': 0,
            'stock': 4,
            'categoria': 'RAM',
        })
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(Producto.objects.exists())
