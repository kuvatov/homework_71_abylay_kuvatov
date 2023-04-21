from django.urls import path, include
from rest_framework import routers

from api.views import PublicationViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register(r'publications', PublicationViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
