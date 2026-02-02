# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('allproducts/', views.product_list, name='product_list'),
    path('addproduct/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    
  
    
    #mambo na customer kuona io cart 
    
    path('addcustomer/', views.customer_create, name='profile_create'),
    path('update/<int:pk>/', views.customer_update, name='profile_update'),
    path('delete/<int:pk>/', views.customer_delete, name='profile_delete'),
    path('login/',views.login_customer,name='logincustomer'),
    
    
    #mambo ya cart    
    path('', views.product_list, name='product_list'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:pk>/', views.update_cart, name='update_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path("cart/remove/<int:pk>/", views.remove_from_cart, name="remove_from_cart"),
   path('get-price/', views.get_price, name='get_price'),

]
