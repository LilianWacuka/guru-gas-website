from django.shortcuts import render
from django.http import HttpResponse
from gurugasspoint.models import Product
from django import forms
from gurugasspoint .forms import ProductForm
from django.shortcuts import redirect
# Create your views here.
def products(request):
    products=Product.objects.all()
    return render(request,'products.html',{'products':products})

def addproduct(request):
    if request.method=="GET":        
        form=ProductForm()
        return render(request,'addproducts.html',{'form':form})
    else:
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('products')

    

def updateproduct(request,id):
    product=Product.objects.get(id=id)
    form=ProductForm(request.POST,instance=product)
    if form.is_valid():
        form.save()
        
    return render(request,'editproducts.html',{'product':product})

def deleteproduct (request,id):
    product=Product.objects.get(id=id)
    product.delete()
    
    
    