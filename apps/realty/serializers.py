from rest_framework import serializers

from realty.models import Realty


class RealtySerializer(serializers.ModelSerializer):
    """Serializer for the reception object."""

    transaction_type_name = serializers.CharField(read_only=True)
    property_type_name: int = serializers.CharField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)
    created = serializers.DateTimeField(read_only=True, format='%Y-%m-%d')

    class Meta:
        model = Realty
        fields = [
            "id",
            "created",
            "user",
            "user_name",
            "client_name",
            "client_phone",
            "phone_agency",
            "phone_agency_name",
            "lessee_phone",
            "transaction_type",
            "transaction_type_name",
            "property_type",
            "property_type_name",
            "region",
            "price",
            "deposit",
            "monthly_rent",
            "memo",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "transaction_type": {"write_only": True},
            "property_type": {"write_only": True},
            "phone_agency": {"write_only": True},
        }

    def create(self, validated_data):
        """Create and return a reception."""

        realty = Realty.objects.create(**validated_data)
        return realty

    def update(self, instance, validated_data):
        """Update and return user."""

        realty = super().update(instance, validated_data)
        return realty