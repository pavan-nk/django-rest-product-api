from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product
from .forms import ProductForm


# Home page – list all products
def home(request):
    products = Product.objects.all().order_by('-created_at')
    context = {
        "products": products,
        "title": "My Products List"
    }
    return render(request, "home.html", context)


# Add a new product
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm()

    return render(request, "add_product.html", {"form": form, "title": "Add Product"})


# Edit an existing product
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm(instance=product)

    return render(request, "edit_product.html", {"form": form, "title": "Edit Product"})
