from django.contrib.auth.models import User
from rest_framework import serializers


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )