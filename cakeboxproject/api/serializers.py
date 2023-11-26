from rest_framework import serializers
from cakebox.models import User,Cakes

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","password","phone","address"]
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)
    

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cakes
        fields="__all__"