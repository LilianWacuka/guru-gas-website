# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('allproducts/', views.product_list, name='product_list'),
    path('addproduct/', views.product_create, name='product_create'),
    path('update/<int:id>/', views.product_update, name='product_update'),
    path('delete/<int:id>/', views.product_delete, name='product_delete'),
    
    #customers
    path('allcustomers/', views.customer_list, name='customer_list'),
    path('addcustomer/', views.customer_create, name='customer_create'),
    path('cus_update/<int:id>/', views.customer_update, name='customer_update'),
    path('cus_delete/<int:id>/', views.customer_delete, name='customer_delete'),
    path('viewproduct/',views.customerview,name="customerview"),
    
    #users
    path('allusers/', views.user_list, name='user_list'),
    path('adduser/', views.user_create, name='user_create'),
    path('user_update/<int:id>/', views.user_update, name='user_update'),
    path('user_delete/<int:id>/', views.user_delete, name='user_delete'),
    
    
    
]



