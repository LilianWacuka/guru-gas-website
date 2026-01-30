# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('allproducts/', views.product_list, name='product_list'),
    path('addproduct/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    
    #customers
    path('allcustomers/', views.customer_list, name='customer_list'),
    path('addcustomer/', views.customer_create, name='customer_create'),
    path('cus_update/<int:pk>/', views.customer_update, name='customer_update'),
    path('cus_delete/<int:pk>/', views.customer_delete, name='customer_delete'),
    path('viewproduct/',views.customerview,name="customerview"),
    
    #users
    path('allusers/', views.user_list, name='user_list'),
    path('adduser/', views.user_create, name='user_create'),
    path('user_update/<int:pk>/', views.user_update, name='user_update'),
    path('user_delete/<int:pk>/', views.user_delete, name='user_delete'),
    
    #login to system
    path('homelogin',views.homelogin,name="homelogin"),
    path('loginform',views.loginform,name="login"),  
    
]



