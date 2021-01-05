from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
#from .form import personal_detalisrForm
#from .models import personal_details
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from costomer.models import order
from products.models import product

# Create your views here.


def register(request):
    if request.method == 'GET':
        u = UserCreationForm()

        d1 = {'u': u}
        return render(request, 'register.html', context=d1)
    elif request.method == 'POST':

        userform = UserCreationForm(request.POST, "NA")
        userform.save()
       # mu =personal_detalisrForm()
            #print(mu)
       # d1 = {'mu': mu}
        #return render(request, 'costomer.html', context=d1)
#ef pd(request):    
#        frm=personal_detalisrForm(request.POST,"NA")
#
#
#
#
#
#frm.save()
        return HttpResponse('your registeration done ')           
  
         


        
def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html') 
   
        # AuthenticationForm_can_also_be_used__ 
    elif request.method=='POST':    
   
        username = request.POST['username'] 
        

        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            login(request, user) 
            request.session['costomer']=username
            request.session['password']=password
            request.session['user_id']=user.id
            

           
            return redirect('home')
        else: 
           
            return render(request,'signin.html')
def logout_view(request):
    logout(request)
    return redirect('home')
#@login_required(login_url='/signin')                
def buy(request):
  #if request.method=='GET':
  #    return render( request,'proceed.html')

    if request.method=='POST':
             
            dict=request.session.get('cart')
            print(dict)
            delete=request.POST.get('delete')
            dict.pop(delete)
            request.session.modified = True
            
            
            print(dict)
           
            return redirect('cart')
def orders(request):
        if request.method=='GET':
            kyes=list(request.session.get('cart'))
            
            products=product.objects.filter(id__in=kyes)
            
            cart=request.session.get('cart')
            qu={}
            for productss in products:
                
                quantity=cart.get(str(productss.id))
                qu['quantity']=quantity
                d1={'products':products,'quantity':quantity}
            
                
            print(qu.get('quantity'))   
            return render(request,'proceed.html',context=d1,)
           
        elif request.method=='POST':
            address=request.POST.get('address')
            phone=request.POST.get('phone')
           # kyes=list(request.session.get('cart').kyes()) why not done?????
            kyes=list(request.session.get('cart').keys())
            product_by_id=product.objects.filter(id__in=kyes)
            cart=request.session.get('cart')
            #(request.session.get('user_id'))
            for products in product_by_id:
                place_order=order(name=request.session.get('costomer'),
                                  phone=phone,
                                  address=address,
                                  product_name=products.name,
                                  price=products.price,
                                  quantity=cart.get(str(products.id)))
                place_order.save()  
            request.session['cart']={}                     
            return redirect('cart')                       
                                        
                                        
                                     
           
            
           
        
       

            
           
           
            
    
    
            

               
     

    
    

    
