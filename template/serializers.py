from rest_framework import serializers
from django.contrib.auth.models import User, Group

from template.models import *


class StatusLeanSerializer(serializers.Serializer):
    detail = serializers.CharField(max_length=120)
    status_lean = serializers.BooleanField(default=False)
    class Meta:
        #model = Wallet
        fields = ('detail', 'status_lean')



class TemplateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Template
        fields = '__all__'