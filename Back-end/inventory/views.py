# -*- coding: utf-8 -*-
# voici les routes à implémenter login, welcome, logout, dashboard
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from inventory.models import User, Product
from django.views.decorators.http import require_POST
# importer les formulaires ici
from inventory.forms import loginForm, productRegister

####################################
# vues pour gestion des utilisateurs
####################################


def loginView(request):
    if request.method == "POST":
        form = loginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)  
                return redirect("dashboard")

            else:
                form.add_error(None, "Identifiants invalides")

    else:
        form = loginForm()

    return render(request, "auth/login.html", {"form": form})

@login_required  
def logoutView(request):
    logout(request)
    return redirect('/login')

@login_required
def me(request):
    user = request.user  # utilisateur déjà authentifié

    print('Utilisateur authentifié avec succès')

    if user.role == 'PDG':
        template = 'dashboard/pdg.html'
    elif user.role == 'STOCK_MANAGER':
        template = 'dashboard/stock_manager.html'
    elif user.role == 'FLUX_MANAGER':
        template = 'dashboard/flux_manager.html'
    else:
        return redirect('login')

    return render(request, template)



####################################
# vues pour gestion des produits
####################################  
@login_required
def productList(request): # pdg et stock manager
    if request.user.role != 'STOCKMANAGER' or request.user.role !='PDG':
        return redirect('unauthorized')
    
    products = Product.objects.filter(is_active=True)
    return # render avec page html des produits et le tableau products en parametres

@login_required
def productCreate(request): # stockmanager

    if request.user.role != 'STOCKMANAGER':
        return redirect('unauthorized')
    
    if request.method == "POST":
        form = productRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('product_list')
        else:
            form = productRegister()

            return # render(request,... ) pour création de produits
        
@login_required
def productUpdate(request, id): #stock manager
    product = get_object_or_404(product, id=id)

    if request.user.role != 'STOCKMANAGER':
        return redirect('unauthorized')
    
    if request.method == 'POST':
        form = productRegister(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('productList')
        
    else:
        form = productRegister(instance=product)

    return # render du produit update.html...form: form

@login_required
@require_POST  # sécurité : suppression seulement via POST
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    # Vérifie que seul un StockManager peut supprimer
    if request.user.role != 'STOCK_MANAGER':
        return redirect('unauthorized')

    # Suppression “soft” : désactiver le produit
    product.is_active = False
    product.save()

    # Ou suppression réelle : product.delete()

    return redirect('product_list')
    


    



####################################
# vues pour gestion des stocks
####################################