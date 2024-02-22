from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu, MenuItem
from restaurant.serializers import MenuSerializer, MenuItemSerializer
from rest_framework import routers
import requests


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        MenuItem.objects.create(title="Menu1", price=10, inventory=50)
        MenuItem.objects.create(title="Menu2", price=15, inventory=30)
        MenuItem.objects.create(title="Menu3", price=20, inventory=20)

    def test_getall(self):
        # Get all Menu objects using the API
        headers = {'Authorization': 'Token f772229e97111a3f7a29979b5e0b5dbb8de658f6'}
        res = requests.get("http://localhost:8000/routers/menu-items/", headers=headers)
        client = APIClient(enforce_csrf_checks=False)
        url = ("http://localhost:8000/routers/menu-items/")
        response = client.get(url,headers=headers)
        menus = MenuItem.objects.all
        serializer = MenuItemSerializer(MenuItem.objects, many=True)

        # Check if the response status code is 200 (OK)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        #self.assertEqual(response, status.HTTP_200_OK)
        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
        