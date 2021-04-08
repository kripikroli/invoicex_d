from rest_framework import serializers

from .models import Client

from apps.invoice.models import Invoice


class ClientInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            "id",
            "invoice_number",
            "is_sent",
            "is_paid",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "get_due_date_formatted",
            "invoice_type",
            "is_credited",
        )


class ClientSerializers(serializers.ModelSerializer):
    invoices = ClientInvoiceSerializer(many=True, read_only=True)

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
            "contact_reference",
            "invoices"
        )
