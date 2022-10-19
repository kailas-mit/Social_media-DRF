from rest_framework import serializers
from .models import Chat
from user_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class ChatSerializer(serializers.ModelSerializer):
    m_sender=serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    m_receiver=serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model=Chat
        fields=('m_sender', 'm_receiver', 'message', 'timestamp')