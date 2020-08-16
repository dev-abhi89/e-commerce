from django.shortcuts import render,redirect
from .models import Product, Category, Cart
from django.http import HttpResponse
from math import ceil





def index(request):

    category = Category.objects.all()
    Jwel = Product.objects.filter(category= 1)[:4]
    spec = Product.objects.filter(category=2)[:4]


    params={'cats':category,'prods':Jwel, 'specs':spec}

    return render(request, 'shop/index.html', params)

def product(request, prod):
    prd = Product.objects.get(id = prod)
    category = Category.objects.all()
    params = {'product': prd, 'p_id':prod, 'cats': category}
    if request.method == 'POST':
        input = request.POST['cart']
        cart = Product.objects.get(id=input)
        entry = Cart(prod_id = cart)
        entry.save()




    return render(request, 'shop/product2.html',params)

def cart(request):
    cat = Category.objects.all()
    cart = Cart.objects.all()
    params = {'cart': cart, 'cats':cat}


    return render(request, 'shop/cart.html', params)

def removeCartobj(request, cartObj):
    object = Cart.objects.get(id=cartObj)
    object.delete()
    return redirect('/shop/cart')




def checkout(request):
    cart = Cart.objects.all()
    cart.delete()
    return redirect('/shop')


def category(request, cats):
    prod = Product.objects.filter(category = cats)
    cat = Category.objects.all()
    params = {'prods': prod,'cat_id':cats, 'cats':cat}
    return render(request, 'shop/category.html', params)

