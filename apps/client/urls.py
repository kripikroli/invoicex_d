from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ClientViewset

router = DefaultRouter()
router.register("clients", ClientViewset, basename="clients")

urlpatterns = [
    path('', include(router.urls)),
]
