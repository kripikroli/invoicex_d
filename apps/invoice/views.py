from rest_framework import viewsets

from .serializers import InvoiceSerializer, ItemSerializer
from .models import Invoice, Item

from django.core.exceptions import PermissionDenied


class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        team = self.request.user.teams.first()
        invoice_number = team.first_invoice_number
        team.first_invoice_number = invoice_number + 1
        team.save()

        serializer.save(created_by=self.request.user, team=team,
                        modified_by=self.request.user, invoice_number=invoice_number, bank_account=team.bank_account)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')

        serializer.save()
