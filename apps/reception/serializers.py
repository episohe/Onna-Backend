from rest_framework import serializers

from realty.models import Realty
from reception.models import Reception


class ReceptionSerializer(serializers.ModelSerializer):
    """Serializer for the reception object."""

    transaction_type_name = serializers.CharField(read_only=True)
    property_type_name = serializers.CharField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)
    created = serializers.DateTimeField(read_only=True, format='%Y-%m-%d')
    state = serializers.ChoiceField(choices=Realty.STATE_CHOICES)
    state_name = serializers.CharField(read_only=True)

    class Meta:
        model = Reception
        fields = [
            'id',
            'created',
            'user',
            'user_name',
            'client_name',
            'client_phone',
            'transaction_type',
            'transaction_type_name',
            'property_type',
            'property_type_name',
            'region',
            'price',
            'deposit',
            'monthly_rent',
            'memo',
            'state',
            'state_name'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'transaction_type': {'write_only': True},
            'property_type': {'write_only': True},
        }

    def create(self, validated_data):
        """Create and return a reception."""
        reception = Reception.objects.create(**validated_data)
        return reception

    def update(self, instance, validated_data):
        """Update and return user."""

        reception = super().update(instance, validated_data)
        return reception
