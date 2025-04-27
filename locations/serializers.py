from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import PointData, PolygonData


class PointDataSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PointData
        geo_field = 'location'
        fields = ('id', 'name', 'description', 'location')


class PolygonDataSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PolygonData
        geo_field = 'boundary'
        fields = ('id', 'name', 'description', 'boundary')