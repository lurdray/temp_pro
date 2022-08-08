from rest_framework import serializers
from django.contrib.auth.models import User, Group

from app_user.models import *


class StatusLeanSerializer(serializers.Serializer):
    detail = serializers.CharField(max_length=120)
    status_lean = serializers.BooleanField(default=False)
    class Meta:
        #model = Wallet
        fields = ('detail', 'status_lean')



class AppUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppUser
        fields = '__all__'