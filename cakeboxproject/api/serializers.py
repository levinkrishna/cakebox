from rest_framework import serializers
from cakebox.models import User,Cakes,CakeVarients,Carts,Orders,Reviews

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","password","phone","address"]
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)
    
class CakevarientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    
    

    class Meta:
        model=CakeVarients
        # 
        exclude=("cake",)

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    
    class Meta:
        model=Reviews
        fields="__all__" 


class CakeSerializer(serializers.ModelSerializer):
    # category=serializers.StringRelatedField(read_only=True)
    category=serializers.SlugRelatedField(slug_field="name",read_only=True)
    varients=CakevarientSerializer(many=True,read_only=True)
    reviews=ReviewSerializer(many=True,read_only=True)
    avg_rating=serializers.CharField(read_only=True)
    class Meta:
        model=Cakes
        fields="__all__"


class CartSerializer(serializers.ModelSerializer):
    cakevarient=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields=["id","cakevarient","user","status","date"]


class OrderSerializer(serializers.ModelSerializer):

    id=serializers.CharField(read_only=True)
    cakevarient=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    orderd_date=serializers.CharField(read_only=True)
    expected_date=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)

    
    class Meta:
        model=Orders
        fields="__all__"


