from django.contrib import admin
from django.urls import path


from . import views
urlpatterns = [
    path('', views.index, name='shop' ),
    path('product/<int:prod>', views.product, name='Product'),
    path('cart', views.cart, name='Cart'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('cart/Cdelete/<int:cartObj>', views.removeCartobj, name='removeObject'),
    path('category/<int:cats>', views.category, name= 'category')




]



