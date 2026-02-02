from django import forms
from gurugasspoint.models import Product,Customer
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = "__all__"