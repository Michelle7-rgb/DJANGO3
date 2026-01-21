from django.urls import path
from inventory import views

urlpatterns = [

    # =====================
    # Racine
    # =====================
    path('', views.home, name='home'),

    # =====================login/
    # Authentification
    # =====================
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),

    # =====================
    # Dashboard
    # =====================
    path('dashboard/', views.me, name='dashboard'),
    path('unauthorized/', views.unauthorizedView, name='unauthorized'),

    # =====================
    # Produits
    # ==========templates===========
    path('products/', views.productList, name='product_list'),
    path('products/create/', views.productCreate, name='product_create'),
    path('products/<int:id>/update/', views.productUpdate, name='product_update'),
    path('products/<int:id>/delete/', views.product_delete, name='product_delete'),
]
