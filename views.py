from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from products.models import product,catogery
from api.serializer import CatogerySerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

 #Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
def api_tamplate(request):
    
    if request.method=='GET':
        return render(request,'api.html')
def api_register(request):
    if request.method=='GET':
        user=UserCreationForm()
        d1={'user':user}
        return render(request,'api_register.html',context=d1)
    elif request.method=='POST':
        user=UserCreationForm(request.POST)
        print(user)
        if user.is_valid:
            user.is_superuser = True
            user.save()
            return HttpResponse('done')

class apisList(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, format=None):
        products = catogery.objects.all()
        serializer = CatogerySerializer(products,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CatogerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
class put(APIView): 
    permission_classes = [permissions.IsAdminUser]  
    def put(self, request, pk, format=None , **kwargs):
        snippet =catogery.objects.get(id=pk)
        serializer = CatogerySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None , **kwargs):
        snippet =catogery.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  