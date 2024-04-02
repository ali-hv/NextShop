from django.test import TestCase

from .factories import ProductFactory, CategoryFactory
from ..models import Product


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), self.category.name)


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = ProductFactory()

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))

    def test_product_str_representation(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_image_url_with_image(self):
        # Create a Product with an image using the ProductFactory
        product_with_image = ProductFactory(image__filename='test_image.jpg')

        # Verify that image_url returns the correct URL for a Product with an image
        expected_url = '/media/products/test_image.jpg'
        self.assertEqual(product_with_image.image_url, expected_url)

    def test_image_url_without_image(self):
        # Create a Product without an image using the ProductFactory
        product_without_image = ProductFactory(image=None)

        # Verify that image_url returns None for a Product without an image
        self.assertIsNone(product_without_image.image_url)
