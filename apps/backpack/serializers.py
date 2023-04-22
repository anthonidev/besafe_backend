from rest_framework import serializers
from .models import BackPack, Element, ElementItem, Food, Health
from django.core.exceptions import ValidationError


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = [
            'id',
            'name',
            'description',
            'icon',
            'type',
        ]


class ElementItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementItem
        fields = [
            'id',
            'count',
            'date_expiration',
        ]

# class FoodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Food
#         fields = [
#             'id',
#             'last_update',
#             'elements',
#         ]
