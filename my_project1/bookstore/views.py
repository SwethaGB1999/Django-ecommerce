from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from . models import *

# Create your views here.

def store(request):
    product=Products.objects.all()
    context={'product':product}
    # if request.method=='POST':
    #     item=Order_item()
    #     item.product=product.product
    #     item.save()
    #     return render(request,'bookstore_cart.html')
    
    return render(request,'bookstore_store.html',context)

# def add_to_cart(request,product_id):
#     product=Products.objects.get(id=product_id)
#     cart_item, created=Order_item.objects.get_or_create(product=product,user=request.user) 
#     cart_item.quantity +=1
#     cart_item.save()        
#     return redirect('/bookstore/store/')

def view_cart(request):
    return render(request,'bookstore_cart.html')


def checkout(request):
    if request.method=='POST':
        obj=Checkout_details()
        obj.name=request.POST.get("name")
        obj.address=request.POST.get("address")
        obj.zip=request.POST.get("zip")
        obj.phone=request.POST.get("phone")
        obj.payment_method = request.POST.get("paymentMethod") or 'cashOnDelivery'
        obj.cardnumber=request.POST.get("cardnumber") or None
        obj.cvv=request.POST.get("cvv") or None
        obj.expirydate=request.POST.get("expirydate") or None
        obj.save()
    return render(request,'bookstore_checkout.html')

def main(request):
    return render(request,'bookstore_main.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm-password')
        if pass1!=pass2:
            return HttpResponse("The passwords do not match! Try again.")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/bookstore/login/')
    return render(request,'bookstore_signup.html')

def log_in(request):
    if request.method=='POST':
        usern=request.POST.get('username')
        pass1=request.POST.get('password')
        print(usern,pass1)
        user=authenticate(request,username=usern,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/bookstore/store/')
        else:
            return HttpResponse('Wrong username or password!')
    
    return render(request,'bookstore_login.html')

def check(request):
    return render(request,'check.html')
