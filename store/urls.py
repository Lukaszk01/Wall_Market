from django.urls import path
from users import views as user_views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.store, name="store"),
  path('register/', user_views.register, name="register"),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
  path('cart/', views.cart, name="cart"),
  path('checkout/', views.checkout, name="checkout"),

  path('update_item/', views.updateItem, name="update_item"),
  path('process_order/', views.processOrder, name="process_order"),
  path('register/', user_views.register, name="register"),
]
