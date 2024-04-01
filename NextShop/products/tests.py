from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name='Test Product',
            slug='test-product',
            description='This is a test product',
            price=10.00,
            stock=5
        )
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.slug, 'test-product')
        self.assertEqual(product.description, 'This is a test product')
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.stock, 5)
