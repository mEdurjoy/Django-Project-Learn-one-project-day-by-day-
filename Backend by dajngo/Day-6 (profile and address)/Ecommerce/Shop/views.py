from django.shortcuts import render
from django.views import View
from httpx import request
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from .models import Customer

# Create your views here.
def home(request):
     return render(request, 'Shop/home.html')

def product_detail(request):
 return render(request, 'Shop/productdetail.html')

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')


def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request):
 return render(request, 'Shop/lehenga.html')



def checkout(request):
 return render(request, 'Shop/checkout.html')


#def customerregistration(request):
# return render(request, 'Shop/customerregistration.html')

class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'Shop/customerregistration.html', {'form':form})
 
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   form.save()
   messages.success(request, 'Congratulations registration successfully done')
  return render(request, 'Shop/customerregistration.html', {'form':form})


#def login(request):
#     return render(request, 'Shop/login.html')

#def profile(request):
# return render(request, 'Shop/profile.html')

class ProfileView(View):
 def get(self, request):
  form = CustomerProfileForm()
  return render(request, 'Shop/profile.html',{'form': form})
 
 def post(self, request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
   usr = request.user
   name = form.cleaned_data['name']
   division = form.cleaned_data['division']
   district = form.cleaned_data['district']
   thana = form.cleaned_data['thana']
   villorroad = form.cleaned_data['villorroad']
   zipcode = form.cleaned_data['zipcode']
   reg = Customer(
     user = usr,
     name = name,
     division = division,
     district = district,
     thana = thana,
     villorroad = villorroad,
     zipcode = zipcode
   )
   reg.save()
   messages.success(request, 'Congratulations! profile update successfully')
  return render(request, 'Shop/profile.html', {'form':form, 'active':'btn-primary'})




def address(request):
  add = Customer.objects.filter(user=request.user)
  return render(request, 'Shop/address.html',{'add':add, 'active':'btn-primary'})
