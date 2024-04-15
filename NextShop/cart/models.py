from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="cart")
    products = models.ManyToManyField(Product, blank=True)

    def get_payable_amount(self):
        # Calculate the total price of cart using aggregation
        total_price = self.products.aggregate(total=models.Sum('price'))['total']
        return total_price or 0  # Return 0 if total_price is None
