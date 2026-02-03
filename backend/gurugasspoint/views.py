from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,Customer
from gurugasspoint.models import Cart
from gurugasspoint.models import CartItem
from gurugasspoint.models import Order
from .forms import ProductForm,CustomerForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



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




#MAMBO MAMBO YA CUSTOMER PALE PALE 

#customer kunda kaprofile
def customer_create(request):
    form = CustomerForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    return render(request, 'customers/createprofile.html', {'form': form})

# UPDATE: Edit an existing customer
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, request.FILES or None, instance=customer)
    if form.is_valid():
        form.save()        
    return render(request, 'customers/editprofile.html', {'form': form})

# DELETE: cudelete profile
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        
    return render(request, 'customers/deleteprofile.html', {'customer': customer})

# kuingia ndani sasaa 

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def myprofile(request):
    return render(request, 'customers/myprofile.html')

def login_view(request):
    msg = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect("/admin/")
            else:
                return redirect("myprofile")
        else:
            msg = "Invalid username or password"

    return render(request, "customers/login.html", {"msg": msg})
def logout_view(request):
    
    logout(request)
    
    return render(request,'customers/login.html')




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

#IO MAMBO YA KADROPDOWN KUCHUKUA WEIGHT
# views.py

def get_price(request):
    weight = request.GET.get('weight')
    try:
        product = Product.objects.get(weight=weight)
        return JsonResponse({'price': float(product.price)})
    except Product.DoesNotExist:
        return JsonResponse({'price': 0})


