from django.test import TestCase
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer
from restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = Menu.objects.create(title="Burger", price=10.99, inventory=50)
        self.menu_item2 = Menu.objects.create(title="Pizza", price=12.99, inventory=40)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

# class MenuViewTest(TestCase):
#     def setUp(self):
#         menu_list = []
#         pizza = Menu.objects.create(title="Pizza", price=80, inventory=100)
#         lasagna = Menu.objects.create(title="Lasagna", price=23, inventory=456)
#         spaguetti = Menu.objects.create(title="Spaguetti", price=58, inventory=123)
#         menu_list.append(pizza)
#         menu_list.append(lasagna)
#         menu_list.append(spaguetti)
#         self.menu_list = menu_list
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username="jacob", email="jacob@…", password="top_secret"
#         )
    
#     def test_getall(self):
#         request = self.factory.get("/api/menu")
#         request.user = self.user
#         response = MenuItemsView.as_view()(request)
#         self.assertEqual(response.status_code, 200)
        
