from rest_framework import serializers
from .models import UserDetails
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ["userid","name","email","phone","address","password"]

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ["userid","password"]




