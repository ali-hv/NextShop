from django.contrib.auth import get_user_model
from django.db import models

from decimal import Decimal

from products.models import Product


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="cart")

    def __str__(self):
        return self.user.username

    @property
    def total_payable_price(self):
        # Calculate the total price for each item and sum up the results
        total_price = sum(item.total_price for item in self.items.all())
        return total_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')  # Ensure only one instance of each product per cart

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart for {self.cart.user}"

    @property
    def total_price(self):
        return self.product.price * Decimal(self.quantity)
