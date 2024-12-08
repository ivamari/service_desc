from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from users.models import ROLE_CHOICES, User


class CustomUserCreateSerializer(UserCreateSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    middle_name = serializers.CharField(required=True)
    role = serializers.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id',
                  'username',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'middle_name',
                  'role', )
