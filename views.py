from django.shortcuts import render,Http404,HttpResponse,redirect
from .models import product,catogery
from .form import productForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.method=='GET':
         ca=catogery.objects.all()
         
         
         #=product.get_all__product()
         catogery_id=request.GET.get('catogery')
         
         obj=product.get_all__product_by_id(catogery_id)
         
         dict=request.session.get('cart')
         
         if dict:

               
               
              # dict={'a':100}
             sum = 0
             for i in dict: 
                 sum= dict[i]+sum
         else:
             dict={'1':0}  
             sum=dict['1']    
               
           
         d1={'product':obj ,'ca':ca,'sum':sum }
           
         return render(request,'index.html',context=d1)

         
         
        
        
   
                  
                 

          
                    
    elif request.method=='POST':
        
        
        product_id=request.POST.get('product')
        quantity=request.POST.get('quantity')
        print(quantity)
        cart=request.session.get('cart')
        
        
          
        if cart:
            quanity=cart.get(product_id)
            if quanity:
                cart[product_id]=quanity+1
            else:
                
                cart[product_id]=1
        else:
            cart={}

            cart[product_id]=1
        request.session['cart']=cart
        return redirect('home')

        
        
        
        
            
                      
                  


                 
                      

                  
            

                    
                        
    

        
                            



       

            
def cart(request):
    if request.method=='GET':
        ca=catogery.objects.all()
        alls=product.get_all__product()
        catogery_id=request.GET.get('catogery')
        obj=product.get_all__product_by_id(catogery_id)
        
        catogery_id=request.GET.get('catogery')
        try:
           kyes=list(request.session.get('cart').keys())
        
        
       
           
           #print('your kyes are',kyes)
           cart_product=product.get_product_by_id(kyes)
           print(cart_product)
          
           
           dict=request.session.get('cart')
           if dict:

               
               
              # dict={'a':100}
                sum = 0
                for i in dict: 
                    sum= dict[i]+sum
           else:
                dict={'1':0}  
                sum=dict['1']    
           d1={'cart_product':cart_product,'product':obj ,'ca':ca,'sum':sum }
           return render(request,'cart.html',context=d1)


        except:
             ca=catogery.objects.all()
         #=product.get_all__product()
             catogery_id=request.GET.get('catogery')
             obj=product.get_all__product_by_id(catogery_id)
             catogery_id=request.GET.get('catogery')
             return render(request,'cart.html',)
                   

                
          
           
          
          
           
               
        
def add(request):
    if request.method=='GET':
        obj=productForm()
        d1={'obj':obj}
        return render(request,'add.html',context=d1)
def query(request):
    query=request.GET['query']
    if len(query)<15:
        allproduct=product.objects.filter(name__icontains=query)
        d1={'allproduct':allproduct,'query':query}
        return render(request,'searchitem.html',context=d1)      
    else:
        allproduct=product.objects.none
        d1={'allproduct':allproduct}
        return render(request,'searchitem.html',context=d1)  
       
    
          
