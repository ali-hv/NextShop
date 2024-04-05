from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from ..serializers import ProductSerializer
from .factories import ProductFactory
from ..models import Product


class ProductViewsTest(TestCase):
    def setUp(self):
        # Create some sample products for testing
        self.product1 = ProductFactory()
        self.product2 = ProductFactory()

        # Initialize Django Client
        self.client = Client()

    def test_list_products(self):
        # Make a GET request to ListProduct view
        response = self.client.get(reverse("products:products_list"))

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the serialized product data
        expected_data = ProductSerializer([self.product1, self.product2], many=True).data
        for item in expected_data:
            item['image'] = 'http://testserver' + item['image']

        self.assertEqual(response.data, expected_data)

    def test_list_products_empty(self):
        # Delete all existing products to simulate an empty queryset
        Product.objects.all().delete()

        # Make a GET request to ListProduct view when there are no products
        response = self.client.get(reverse("products:products_list"))

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains an empty list of products
        self.assertEqual(response.data, [])
