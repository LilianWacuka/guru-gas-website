from django.urls import path
from .import views
urlpatterns = [
    
    path('',views.home,name="loginhome"),
    path('kaform/',views.loginform,name="login"),
    
]
