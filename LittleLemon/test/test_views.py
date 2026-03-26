from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Añadimos instancias de prueba
        Menu.objects.create(title="Pizza", price=15, inventory=50)
        Menu.objects.create(title="Burger", price=10, inventory=30)

    def test_getall(self):
        # Obtenemos todos los objetos
        items = Menu.objects.all()
        # Los serializamos
        serialized_data = MenuSerializer(items, many=True).data
        # Verificamos que se hayan creado 2 elementos
        self.assertEqual(len(serialized_data), 2)
        # Verificamos el nombre del primero
        self.assertEqual(serialized_data[0]['title'], "Pizza")
