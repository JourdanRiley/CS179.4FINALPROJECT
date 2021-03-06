from .models import User, Product, Cart, Holidate
from django.http import Http404
import django.contrib.staticfiles
from .serializers import UserSerializer, CartSerializer, ProductSerializer, HolidateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse

def home(request):
	return render(request, 'FinalProject/index.html', {})

class UserList(APIView):
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many = True)
		return Response(serializer.data)
		
	def post(self, request, format = None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
class UserDetail(APIView):
	
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(user.data)
	
	def put(self, request, pk, format = None):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data = data.request)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format = None):
		user = self.get_object(pk)
		user.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
		
class CartList(APIView):
	def get(self, request, format=None):
		carts = Cart.objects.all()
		serializer = CartSerializer(carts, many = True)
		return Response(serializer.data)
		
	def post(self, request, format = None):
		serializer = CartSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
class CartDetail(APIView):
	
	def get_object(self, pk):
		try:
			return Cart.objects.get(pk=pk)
		except Cart.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		cart = self.get_object(pk)
		serializer = CartSerializer(cart)
		return Response(cart.data)
	
	def put(self, request, pk, format = None):
		cart = self.get_object(pk)
		serializer = CartSerializer(cart, data = data.request)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format = None):
		cart = self.get_object(pk)
		cart.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)
		
class ProductList(APIView):
	def get(self, request, format=None):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many = True)
		return Response(serializer.data)
		
	def post(self, request, format = None):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
class ProductDetail(APIView):
	
	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		product = self.get_object(pk)
		serializer = ProductSerializer(product)
		return Response(product.data)
	
	def put(self, request, pk, format = None):
		product = self.get_object(pk)
		serializer = ProductSerializer(product, data = data.request)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format = None):
		product = self.get_object(pk)
		product.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)

class HolidateList(APIView):
	def get(self, request, format=None):
		holidates = Holidate.objects.all()
		serializer = HolidateSerializer(holidates, many = True)
		return Response(serializer.data)
		
	def post(self, request, format = None):
		serializer = HolidateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	
		
class HolidateDetail(APIView):
	
	def get_object(self, pk):
		try:
			return Holidate.objects.get(pk=pk)
		except Holidate.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		holidate = self.get_object(pk)
		serializer = HolidateSerializer(holidate)
		return Response(holidate.data)
	
	def put(self, request, pk, format = None):
		holidate = self.get_object(pk)
		serializer = HolidateSerializer(holidate, data = data.request)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format = None):
		holidate = self.get_object(pk)
		holidate.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)