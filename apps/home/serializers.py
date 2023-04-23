from rest_framework import serializers
from .models import HomeGroup, Floor
from django.core.exceptions import ValidationError


class FloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = ['id', 'number', 'safe_zone', 'picture']


class HomeGroupSerializer(serializers.ModelSerializer):
    floors = FloorSerializer(many=True, read_only=True)

    class Meta:
        model = HomeGroup
        fields = (
            'id',
            'name',
            'description',
            'build_year',
            'build_material',
            'family_code',
            'floors'

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
