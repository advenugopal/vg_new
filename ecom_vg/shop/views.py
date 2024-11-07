from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Products
from django.contrib import messages
from .forms import ProductForm
from django.shortcuts import render, redirect

#CRUD= CREATE,READ, UPDATE, DELETE

def home(request):

    products=Products.objects.all()

    return render(request,'home.html',{'products':products})

def add_product(request):
    if request.method == 'POST':
        productform=ProductForm(request.POST,request.FILES)
        if productform.is_valid():
            productform.save()
            messages.success(request,"Succesfully added new product")
    productform=ProductForm()
    return render(request,'add_product.html', {'form':productform})


def edit_product(request, product_id):
    # products=Products.objects.filter(name="samsung s9").update(stock=40)


    product=get_object_or_404(Products, id=product_id)
    if request.method=='POST':
        product_form=ProductForm(request.POST,request.FILES,instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
    product_form=ProductForm(instance=product)
    return render(request,'edit_product.html',{'form':product_form})

def delete_product(request,pk):

    product=Products.objects.get(pk=pk)
    product.delete()
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']

        myuser= User.objects.create_user(username=username,password=password1,email=email)
        print(myuser)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password1 = request.POST['password1']
        user= authenticate(username=username,password=password1)
        print(user)
        if user is not None:
            login(request,user)
            fname=user.first_name
            lname=user.last_name
            return render(request,'user_dashboard.html',{'fname':fname,'lname':lname})
        else:
            messages.error(request,"Invalid credential")
            return redirect('signin')

    return render(request,'signin.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from . models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    print(f"Session Key: {cart}")
    return cart

def add_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_id = _cart_id(request)
    if not cart_id:
        return redirect('cart_detail')

    cart, created = Cart.objects.get_or_create(cart_id=cart_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart, defaults={'quantity': 1})

    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')


def cart_detail(request):
    total = 0
    counter = 0
    cart_items = None

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except Cart.DoesNotExist:
        pass

    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total, 'counter': counter})


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = get_object_or_404(CartItem, product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_detail')


def full_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = get_object_or_404(CartItem, product=product, cart=cart)
    cart_item.delete()

    return redirect('cart_detail')
