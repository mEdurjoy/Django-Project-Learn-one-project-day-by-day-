from django.urls import path
from Shop import views
from django.contrib.auth import views as auth_views
from .forms import MyLoginForm, MyPasswordChangeForm
urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('lehenga/', views.lehenga, name='lehenga'),
    
    
    path('checkout/', views.checkout, name='checkout'),






    # authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    #path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='Shop/login.html', authentication_form=MyLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #Change password
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='Shop/changepassword.html', form_class=MyPasswordChangeForm, success_url='/'), name='changepassword'),
    #path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='Shop/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

]