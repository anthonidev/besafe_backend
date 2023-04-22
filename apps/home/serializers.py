from rest_framework import serializers
from .models import HomeGroup
from django.core.exceptions import ValidationError


class HomeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeGroup
        fields = (
            'id',
            'name',
            'description',
            'build_year',
            'build_material',
            'family_code',

        )

    def create(self, validated_data):
        validate_account_data(validated_data)
        return HomeGroup.objects.create(**validated_data)


def validate_account_data(data):
    required_fields = {
        'name': 'Phone number is required',
        'description': 'Date of birth is required',
        'build_year': 'DNI is required',
        'build_material': 'First name is required',
    }
    errors = {}

    for field, message in required_fields.items():
        if not data.get(field):
            errors[field] = message
    if errors:
        raise ValidationError(errors)
