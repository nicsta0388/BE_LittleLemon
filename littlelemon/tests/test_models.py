from django.test import TestCase
from restaurant.models import Menu, MenuItem

class MenuItemTest(TestCase):
    def test_get_menu_item(self):
        item = MenuItem.objects.create(title="Pasta", price="20")
        crossCheck = "Pasta : 20"
        self.assertEqual(str(item), crossCheck)

class MenuModelTest(TestCase):
    def test_create_menu(self):
        # create a new menu object
        menu = Menu.objects.create(title='Breakfast', price=20, description='A selection of breakfast items')

        # check that the string representation of the object is as expected
        self.assertEqual(str(menu), 'Breakfast : 20 , A selection of breakfast items')

        # check that the name, price, and description fields are set correctly
        self.assertEqual(menu.title, 'Breakfast')
        self.assertEqual(menu.price, 20)
        self.assertEqual(menu.description, 'A selection of breakfast items')

