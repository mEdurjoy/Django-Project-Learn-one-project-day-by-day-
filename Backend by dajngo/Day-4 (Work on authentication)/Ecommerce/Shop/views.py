from django.shortcuts import render
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages 

# Create your views here.
def home(request):
     return render(request, 'Shop/home.html')

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


def checkout(request):
 return render(request, 'Shop/checkout.html')


#authentication

class Customerregistration(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'Shop/customerregistration.html', {'form': form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'Shop/customerregistration.html', {'form': form})

#def login(request):
#     return render(request, 'Shop/login.html')
