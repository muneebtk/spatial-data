from django.urls import path, include
from rest_framework.routers import DefaultRouter
from locations.views import PointDataViewSet, PolygonDataViewSet

router = DefaultRouter()
router.register(r'points', PointDataViewSet, basename='pointdata')
router.register(r'polygons', PolygonDataViewSet, basename='polygondata')


urlpatterns = [
    path('api/', include(router.urls)),
]
