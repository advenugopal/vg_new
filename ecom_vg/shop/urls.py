
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_product/', views.add_product, name="add_prod"),
    path('edit_product/<int:product_id>/', views.edit_product, name="edit_product"),
    path('delete_product/<int:pk>/', views.delete_product, name="delete_product"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('cart/',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'),

]