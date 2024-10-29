from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data)['password']
        return super().create(validated_data)