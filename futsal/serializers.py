from rest_framework import serializers
from .models import User, Futsal, Booking

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
    class Meta:
        model = User
        fields = 'user_phone','user_role','id','username','email','first_name','last_name','password'
        
        
class FutsalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Futsal
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
    