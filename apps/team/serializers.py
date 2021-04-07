from rest_framework import serializers

from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = (
            "created_by",
        ),
        fields = (
            "id",
            "name",
            "company_number",
            "first_invoice_number",
            "bank_account",
            "email",
            "address_line_1",
            "address_line_2",
            "city_name",
            "state_name",
            "country_name",
            "zip_code"

        )
