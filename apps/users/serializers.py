import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def email_validator(value):
    if re.match(".*@sansano.usm.cl", value):
        return value
    else:
        raise ValidationError("Usuario no válido.")


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255, validators=[email_validator])
    password = serializers.CharField(max_length=256)
