from django.urls import path
from Shop import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('', views.home, name='home'),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('lehenga/', views.lehenga, name='lehenga'),
    path('checkout/', views.checkout, name='checkout'),

    # authentication
    path('registration/', views.Customerregistration.as_view(), name='customerregistration'),
    path('login/', auth_views.LoginView.as_view(template_name= 'Shop/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]