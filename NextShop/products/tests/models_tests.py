from django.test import TestCase

from .factories import ProductFactory
from ..models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = ProductFactory()

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
