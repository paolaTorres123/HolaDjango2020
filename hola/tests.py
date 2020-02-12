from django.test import TestCase
from hola.models import Articulo
from django.core.exceptions import ValidationError
from hola.forms import FormArticulo

# Create your tests here.
class TestSmoke(TestCase):
    def test_smoke_Test(self):
        self.assertEqual(2+2,4)

class TestModels(TestCase):
    def setUp(self):
        self.articulo = Articulo(
            nombre ='Juguete',
            precio=120.55,
            descripcion='Juguete bonito'
        )
        self.articulo.save()
    def test_agrega_articulo(self):
        self.articulo.save()
        self.assertEqual(Articulo.objects.count(),1)
    def test_agrega_nombre_act_vacio(self):
        self.articulo.save()
        self.articulo.nombre=''
        with self.assertRaises(ValidationError):
            self.articulo.full_clean()
class TestForms(TestCase):
    def setUp(self,nombre="Juguete",precio=120.55,descripcion="Juguete bonito"):
        
        self.data={
            'nombre':nombre,
            'precio':precio,
            'descripcion':descripcion

        }
    def test_formarticulo_valido(self):
        form = FormArticulo(
            self.data
        )
        self.assertTrue(form.is_valid())

    def test_nombre_act_vacio(self):
        self.data['nombre']=''
        form=FormArticulo(
            self.data
        )
        self.assertFalse(form.is_valid())

class TestViews(TestCase):
    def setUp(self,nombre="Juguete",precio=120.55,descripcion="Juguete bonito"):
        self.data={
            'nombre':nombre,
            'precio':precio,
            'descripcion':descripcion

        }
    '''def test_url_articulos_alta(self):
        response = self.client.get('/articulo/articulos')
        self.assertEqual(response.status_code,200)'''

    


