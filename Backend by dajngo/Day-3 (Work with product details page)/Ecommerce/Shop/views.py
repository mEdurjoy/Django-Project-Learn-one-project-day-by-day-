from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.
#def home(request):
#     return render(request, 'Shop/home.html')

class ProductView(View):
     def get(self, request):
          saree = Product.objects.filter(category='S')
          lehenga = Product.objects.filter(category='L')
          topwear = Product.objects.filter(category='TW')
          return render(request, 'Shop/home.html', {'sarees': saree, 'lehengas': lehenga, 'topwears': topwear})

#def product_detail(request):
# return render(request, 'Shop/productdetail.html')

class product_detail(View):
     def get(self, request, pk):
          product = Product.objects.get(pk=pk)
          return render(request, 'Shop/productdetail.html', {'product': product})

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

def lehenga(request, data=None):
 if data== None:
   lehengas = Product.objects.filter(category='L')
 elif data == 'Lubnan' or data== 'Aarong':
  lehengas = Product.objects.filter(category='L').filter(brand=data)
 return render(request, 'Shop/lehenga.html', {'lehengas': lehengas})


def saree(request, data=None):
 if data== None:
   sarees = Product.objects.filter(category='S')
 elif data == 'Jamdani' or data== 'Aarong' or data== 'Pakistani':
  sarees = Product.objects.filter(category='S').filter(brand=data)
 return render(request, 'Shop/saree.html', {'sarees': sarees})

def login(request):
     return render(request, 'Shop/login.html')

def customerregistration(request):
 return render(request, 'Shop/customerregistration.html')

def checkout(request):
 return render(request, 'Shop/checkout.html')
