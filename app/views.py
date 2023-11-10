

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer , CategorySerializer
from .models import Category, Product 
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework import status








# Create your views here.
@api_view(['GET'])
def index(request):
    return Response("Hola a todos!")




@api_view(['GET','POST','DELETE','PUT','PATCH'])
def product(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_product=Product.objects.get(id=id)
                return Response (ProductSerializer(temp_product,many=False).data)
            except Product.DoesNotExist:
                return Response ("not found")
        all_products=ProductSerializer(Product.objects.all(),many=True).data
        return Response ( all_products)
    if req.method =='POST':
        tsk_serializer = ProductSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("post...")
        else:
            return Response (tsk_serializer.errors)
    if req.method =='DELETE':
        try:
            temp_product=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response ("not found")    
       
        temp_product.delete()
        return Response ("del...")
    if req.method == 'PUT':
        try:
            temp_product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response("not found")

        # Create a ProductSerializer instance with the existing product and the request data
        ser = ProductSerializer(temp_product, data=req.data)

        if ser.is_valid():
            # Save the updated product
            ser.save()
            return Response("put...")
        else:
            return Response(ser.errors)

    



class Category_view(APIView):
    def get(self, request):
        my_model = Category.objects.all()
        serializer = CategorySerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = CategorySerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        try:
            my_model = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
       
    def delete(self, request, pk):
        my_model = Category.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # ...
        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# register
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")




@api_view(['get'])
@permission_classes([IsAuthenticated])
def getCart(req):
    return Response("now you can see the cart")