# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,Customer,User
from .forms import ProductForm,CustomerForm,UserForm

# READ: List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/allproducts.html', {'products': products})

# CREATE: Add a new product
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/addproducts.html', {'form': form})

# UPDATE: Edit an existing product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
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
    return render(request, 'allproducts.html', {'product': product})

#  MAMABO YA  CUSTOMER KWA DATABASE
# READ: List all products
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/allcustomers.html', {'customers': customers})

# CREATE: Add a new customer
def customer_create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'customers/addcustomer.html', {'form': form})

# UPDATE: Edit an existing Customer
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'customers/editcustomer.html', {'form': form})

# DELETE: Remove a Customer
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers_list')
    return render(request, 'customer/allcustomers.html', {'customer': customer})

#  MAMABO YA  users KWA DATABASE
# READ: List all USERS
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/allusers.html', {'users': users})

# CREATE: Add a new user
def user_create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'users/adduser.html', {'form': form})

# UPDATE: Edit an existing user
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = CustomerForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'users/edituser.html', {'form': form})

# DELETE: Remove a user
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users_list')
    return render(request, 'users/allusers.html', {'user': user})


