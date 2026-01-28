# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# READ: List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'allproducts.html', {'products': products})

# CREATE: Add a new product
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'addproducts.html', {'form': form})

# UPDATE: Edit an existing product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'editproducts.html', {'form': form})

# DELETE: Remove a product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'allproducts.html', {'product': product})
