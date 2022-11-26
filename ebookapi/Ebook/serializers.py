from rest_framework import serializers
from .models import Ebooks,Rating
from django.contrib.auth import get_user_model

User=get_user_model()
class UserRegister(serializers.ModelSerializer):
    requires_context = True
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=User
        fields=["username","password","email","password2"]
        
    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
class EbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebooks
        fields ="__all__"
class RatingSerializer(serializers.ModelSerializer):
    # Title=EbooksSerializer()
    class Meta:
        model = Rating
        fields="__all__"
