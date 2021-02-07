from rest_framework import serializers
from .models import Flight,Passenger,Reservation
import re  #validation1
'''
def urWishName(data):                               #validation3
    print(data)
    print("isFlightNumberValid")
'''
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
        #validators = [urWishName]                  #validation3
        
    def validate_flightNumber(self,flightNumber):   #validation1
        if(re.match("^[a-zA-Z0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("Invalid Flight Number. Make sure it is alpha numeric")
        return flightNumber

        
    '''
    def validate(self,data):                        #validation2
        print("validate")
        print(data['flightNumber'])
        return data
    '''    
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"