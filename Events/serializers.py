from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Event

class EventSerializer(serializers.ModelSerializer):
      class Meta:
        model = Event
        fields = ["user", "id", "title", "description", "date_and_time"]
        read_only_fields = ['user']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user        