
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from gurugasspoint.models import Cart
from gurugasspoint.models import CartItem
from gurugasspoint.models import Order
from .forms import ProductForm

# READ: List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/allproducts.html', {'products': products})

# CREATE: Add a new product
def product_create(request):
    form = ProductForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/addproducts.html', {'form': form})

# UPDATE: Edit an existing product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/editproducts.html', {'form': form})

# DELETE: Remove a product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/deleteproduct.html', {'product': product})

#customer kuchungulia mali
def viewproducts(request):
    products = Product.objects.all()
    return render(request,'products/customerview.html',{'products':products})




# MAMBO MAMABO YA CART PALEEE KWENYEWE
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem,OrderItem

def get_cart(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = get_cart(request)
    quantity = int(request.POST.get('quantity', 1))

    item = CartItem.objects.filter(cart=cart, product=product).first()
    if item:
        item.quantity += quantity
        item.save()
    else:
        CartItem.objects.create(cart=cart, product=product, quantity=quantity)

    return redirect('cart_detail')

def update_cart(request, pk):
    cart = get_cart(request)
    item = get_object_or_404(CartItem, pk=pk, cart=cart)

    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()

    return redirect("cart_detail")

def cart_detail(request):
    cart = get_cart(request)
    items = cart.items.all()
    return render(request, 'cart/detail.html', {
        'cart': cart,
        'items': items,
    })
def checkout(request):
    cart = get_cart(request)
    items = cart.items.all()

    if not items:
        return redirect('cart_detail')

    # Create a new Order
    order = Order.objects.create(total_price=cart.total_price())

    # Copy cart items into OrderItems
    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price  # snapshot of price at purchase time
        )

    # Clear the cart after checkout
    cart.items.all().delete()

    return render(request, 'cart/checkout_success.html', {'order': order})

def remove_from_cart(request, pk):
    cart = get_cart(request)
    try:
        item = CartItem.objects.get(pk=pk, cart=cart)
        if request.method == "POST":
            item.delete()
    except CartItem.DoesNotExist:
        # Optionally just ignore if item not found
        pass
    return redirect("cart_detail")



