from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

# -------------------
# Utilisateur
# -------------------
class User(AbstractUser):
    ROLE_CHOICES = [
        ('PDG', 'PDG'),
        ('STOCK_MANAGER', 'Gestionnaire de stock'),
        ('FLUX_MANAGER', 'Gestionnaire des flux'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


# -------------------
# Produits et Stock
# -------------------
class Product(models.Model):
    name = models.CharField(max_length=150)
    reference = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    alert_threshold = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.reference})"


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

# -------------------
# Mouvements de stock
# -------------------
class StockMovement(models.Model):
    MOVEMENT_TYPE = [
        ('IN', 'Entrée'),
        ('OUT', 'Sortie'),
        ('TRANSFER', 'Transfert'),
    ]

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPE)
    quantity = models.PositiveIntegerField()
    performed_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        limit_choices_to={'role': 'FLUX_MANAGER'}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.movement_type} - {self.product.name} ({self.quantity})"


