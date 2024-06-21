from django.test import TestCase
from app.models import Product


class TestProduct(TestCase):
    def test_item_creation(self):
        product = Product.objects.create(item="Milk", stock=10)
        self.assertEqual(str(product), "Milk")
        self.assertEqual(product.stock, 10)
