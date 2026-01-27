
from django.urls import path
from .import views


urlpatterns = [
    path('viewproducts/',views.products,name="products"),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('<int:id>/',views.deleteproduct,name="deleteproduct"),
    path('<int:id>/',views.updateproduct,name="updateproduct")
]
