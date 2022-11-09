from rest_framework import serializers

from reception.models import Reception


class ReceptionSerializer(serializers.ModelSerializer):
    """Serializer for the reception object."""

    transaction_type_name = serializers.CharField(read_only=True)
    property_type_name = serializers.CharField(read_only=True)

    class Meta:
        model = Reception
        fields = [
            "id",
            "user",
            "client_name",
            "client_phone",
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
        }
