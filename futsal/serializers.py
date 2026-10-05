from datetime import datetime
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
        
        if not futsal.f_is_active:
            raise serializers.ValidationError("This Futsal is not active at the moment")
        
        starting_time = data['starting_time']
        ending_time = data['ending_time']
        
        if starting_time < futsal.f_opening_time or ending_time > futsal.f_closing_time:
            raise serializers.ValidationError("Booking is only available during operating hours.")
        
        if ending_time <= starting_time:
            raise serializers.ValidationError("Starting time must be earlier than ending time.")
        
        if starting_time.minute != 0 or ending_time.minute != 0:
            raise serializers.ValidationError("Bookings must start and end on a full hour." )   
        
        starting_datetime = datetime.combine(data['date'], starting_time)
        ending_datetime = datetime.combine(data['date'], ending_time)
        
        duration =  ending_datetime - starting_datetime
        hours = int(duration.total_seconds() / 3600)
        if game_type == '5A':
            total_price = hours * futsal.f_price_5a
        if game_type == '7A':
            total_price = hours * futsal.f_price_7a
        
        data['total_price'] = total_price

        
        existing_booking = Booking.objects.filter(futsal = futsal , date=data['date']).exclude(status = "cancelled")
        
        for booking in existing_booking:
            if starting_time < booking.ending_time and ending_time > booking.starting_time :
                raise serializers.ValidationError("This time is already booked. Please book at different time.")
            
        return data

        
        
            
            
            

    
    class Meta:
        model = Booking
        fields = '__all__'
    