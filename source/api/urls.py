from django.urls import path, include
from rest_framework import routers

from api.views import PublicationViewSet

router = routers.DefaultRouter()
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
