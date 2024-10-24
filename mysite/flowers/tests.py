from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Order

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Test Product", price=10.00)

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.price, 10.00)

class OrderTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        product = Product.objects.create(name="Test Product", price=10.00)
        order = Order.objects.create(user=user)
        order.products.add(product)

    def test_order_creation(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.user.username, "testuser")
        self.assertEqual(order.products.count(), 1)
