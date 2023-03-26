from django.urls import path
from .import views
from .forms import *

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:towns_slug>', views.home, name='hostels_by_towns'),
    path('create/', views.signUpView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.signoutView, name='signout'),
    path('hostel/<int:hostel_id>', views.hostels, name='hostel_detail'),
    path('myacount/', views.myacount, name='myacount'),
    path('settlement/<int:hostel_id>', views.settlement, name='settlement'),
    path('settlement_cancil/', views.settlement_cancil, name='settlement_cancil'),
    
   
]