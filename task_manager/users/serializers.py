from rest_framework import serializers
from django.contrib.auth.models import User

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims (Username of the User in the token)
#         token["username"] = user.username
#         # ...

#         return token


# class UserResgisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "username", "email", "password")

#     extra_kwargs = {
#         "first_name": {"required": True, "allow_blank": False},
#         "last_name": {"required": True, "allow_blank": False},
#         "username": {"required": True, "allow_blank": False},
#         "email": {"required": True, "allow_blank": False},
#         "password": {"required": True, "allow_blank": False},
#     }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
