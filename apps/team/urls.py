from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewset

router = DefaultRouter()
router.register("teams", TeamViewset, basename="teams")

urlpatterns = [
    path('', include(router.urls)),
]
