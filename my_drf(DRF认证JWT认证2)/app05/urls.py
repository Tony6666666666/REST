from django.urls import path

from app05 import views

urlpatterns=[
    path(r'carts/',views.CartView.as_view(),name='cart-list'),
    path(r'login/',views.LoginView.as_view(),name='login'),
]