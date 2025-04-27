from rest_framework.viewsets import ModelViewSet
from .models import PointData, PolygonData
from .serializers import PointDataSerializer, PolygonDataSerializer


class PointDataViewSet(ModelViewSet):
    queryset = PointData.objects.all()
    serializer_class = PointDataSerializer


class PolygonDataViewSet(ModelViewSet):
    queryset = PolygonData.objects.all()
    serializer_class = PolygonDataSerializer