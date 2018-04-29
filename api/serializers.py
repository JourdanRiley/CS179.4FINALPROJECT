from rest_framework import serializers
from .models import User, Cart, Product, Holidate

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class CartSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cart
		fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'		
		
class HolidateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Holidate
		fields = '__all__'	