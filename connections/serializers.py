from urllib import response
from rest_framework import serializers
from .models import Connection
from rest_framework.response import Response

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Connection
        fields='__all__'
        extra_kwargs={'sender':{'default': serializers.CurrentUserDefault()}}




class ConnectingSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=True)
    class Meta:
        model=Connection
        fields='__all__'
        extra_kwargs={'recever':{'default': serializers.CurrentUserDefault()}}
