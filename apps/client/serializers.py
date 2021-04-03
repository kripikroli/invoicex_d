from rest_framework import serializers

from .models import Client


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = (
            "created_at",
            "created_by",
        ),
        fields = (
            "id",
            "name",
            "email",
            "company_number",
            "address_line_1",
            "address_line_2",
            "city_name",
            "state_name",
            "country_name",
            "zip_code",
            "contact_person",
            "contact_reference"
        )
