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
    def validate(self, data):
        game_type = data['game_type']
        futsal = data['futsal']
        if game_type == '5A' and not futsal.f_supports_5a:
            raise serializers.ValidationError()
        if game_type == '7A' and not futsal.f_supports_7a:
            raise serializers.ValidationError()
        
        starting_time = data['starting_time']
        ending_time = data['ending_time']
        
        if starting_time < futsal.f_opening_time or ending_time > futsal.f_closing_time:
            raise serializers.ValidationError("Booking is only available during operating hours.")
            
        return data

        
        
            
            
            

    
    class Meta:
        model = Booking
        fields = '__all__'
    