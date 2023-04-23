from rest_framework import serializers
from .models import Account
from django.core.exceptions import ValidationError


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id',  'phone', 'dob', 'dni', 'first_name', 'last_name', 'gender'

                  )

    def create(self, validated_data):
        validate_account_data(validated_data)
        return Account.objects.create(**validated_data)


def validate_account_data(data):
    required_fields = {
        'phone': 'Phone number is required',
        'dob': 'Date of birth is required',
        'dni': 'DNI is required',
        'first_name': 'First name is required',
        'last_name': 'Last name is required',
        'gender': 'gender is required',
    }
    errors = {}

    for field, message in required_fields.items():
        if not data.get(field):
            errors[field] = message
    if errors:
        raise ValidationError(errors)
