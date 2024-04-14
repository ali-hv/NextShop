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
        response = self.client.get(reverse("products:product_list"))

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the serialized product data
        expected_data = ProductSerializer([self.product1, self.product2], many=True).data

        # Convert image urls to absolute urls in expected data
        for item in expected_data:
            item['image'] = 'http://testserver' + item['image']

        # Check that response data and expected data are equal
        self.assertEqual(response.data, expected_data)

    def test_list_products_empty(self):
        # Delete all existing products to simulate an empty queryset
        Product.objects.all().delete()

        # Make a GET request to ListProduct view when there are no products
        response = self.client.get(reverse("products:product_list"))

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains an empty list of products
        self.assertEqual(response.data, [])

    def test_detail_product(self):
        # Make a GET request to DetailProduct view
        response = self.client.get(reverse("products:product_detail",
                                           args=[self.product1.id]))

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the serialized product data
        expected_data = ProductSerializer(self.product1).data

        # Convert image url to absolute url in expected data
        expected_data['image'] = 'http://testserver' + expected_data['image']

        # Check that response data and expected data are equal
        self.assertEqual(response.data, expected_data)
