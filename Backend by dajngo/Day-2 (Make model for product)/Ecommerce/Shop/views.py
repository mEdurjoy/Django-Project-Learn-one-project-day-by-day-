from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.
#def home(request):
#    return render(request, 'Shop/home.html')

class ProductView(View):
 def get(self, request):
  gentspant = Product.objects.filter(category='GP')
  borka = Product.objects.filter(category='BK')
  babyfashion = Product.objects.filter(category='BF')
  return render(request, 'Shop/home.html',{'gentspants':gentspant, 'borkas':borka, 'babyfashions':babyfashion})

def product_detail(request):
 return render(request, 'Shop/productdetail.html')

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')

def profile(request):
 return render(request, 'Shop/profile.html')

def address(request):
 return render(request, 'Shop/address.html')

def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request):
 return render(request, 'Shop/lehenga.html')

def login(request):
     return render(request, 'Shop/login.html')

def customerregistration(request):
 return render(request, 'Shop/customerregistration.html')

def checkout(request):
 return render(request, 'Shop/checkout.html')
