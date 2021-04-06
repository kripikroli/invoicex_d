from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import InvoiceViewset

router = DefaultRouter()
router.register("invoices", InvoiceViewset, basename="invoices")

urlpatterns = [
    path('', include(router.urls)),
]
