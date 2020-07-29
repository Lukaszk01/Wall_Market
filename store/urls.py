from django.urls import path
from users import views as user_views
from . import views

urlpatterns = [
  path('', views.store, name="store"),
  path('register/', user_views.register, name="register"),
  path('cart/', views.cart, name="cart"),
  path('checkout/', views.checkout, name="checkout"),

  path('update_item/', views.updateItem, name="update_item"),
  path('process_order/', views.processOrder, name="process_order"),
  path('register/', user_views.register, name="register"),
]
