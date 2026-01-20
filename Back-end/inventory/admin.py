from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Product, Stock, StockMovement


# ------------------------
# User personnalisé
# ------------------------
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Rôle', {'fields': ('role',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Rôle', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')


# ------------------------
# Produit
# ------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'reference', 'category', 'purchase_price', 'sale_price', 'alert_threshold', 'is_active')
    search_fields = ('name', 'reference', 'category')
    list_filter = ('category', 'is_active')


# ------------------------
# Stock
# ------------------------
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
    search_fields = ('product__name', 'product__reference')


# ------------------------
# Mouvements de stock
# ------------------------
@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity', 'performed_by', 'created_at')
    list_filter = ('movement_type', 'performed_by')
    search_fields = ('product__name', 'performed_by__username')
    readonly_fields = ('created_at',)

    # Interdire la suppression pour protéger l'historique des fluxs
    def has_delete_permission(self, request, obj=None):
        return False
