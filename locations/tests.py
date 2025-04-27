# Create your tests here.
import pytest
from django.contrib.gis.geos import Point, Polygon
from locations.models import PointData, PolygonData


@pytest.mark.django_db
def test_create_point_model():
    """Test creating a PointData instance."""
    point = Point(x=12.4924, y=41.8902)  # Longitude, Latitude
    point_instance = PointData.objects.create(name="Sample Point", location=point)
    
    assert PointData.objects.count() == 1
    assert point_instance.name == "Sample Point"
    assert point_instance.location.equals(point)

@pytest.mark.django_db
def test_create_polygon_model():
    """Test creating a PolygonModel instance."""
    polygon = Polygon(
        (
            (12.4924, 41.8902),
            (12.4924, 41.8912),
            (12.4934, 41.8912),
            (12.4934, 41.8902),
            (12.4924, 41.8902),
        )
    )
    polygon_instance = PolygonData.objects.create(name="Sample Polygon", boundary=polygon)
    
    assert PolygonData.objects.count() == 1
    assert polygon_instance.name == "Sample Polygon"
    assert polygon_instance.boundary.equals(polygon)

@pytest.mark.django_db
def test_point_within_polygon():
    """Test if a point is within a polygon."""
    polygon = Polygon(
        (
            (12.4924, 41.8902),
            (12.4924, 41.8912),
            (12.4934, 41.8912),
            (12.4934, 41.8902),
            (12.4924, 41.8902),
        )
    )
    PolygonData.objects.create(name="Test Polygon", boundary=polygon)

    point_inside = Point(x=12.493, y=41.8905)
    point_outside = Point(x=12.494, y=41.892)

    assert PolygonData.objects.filter(boundary__contains=point_inside).exists()
    assert not PolygonData.objects.filter(boundary__contains=point_outside).exists()

@pytest.mark.django_db
def test_polygon_intersection():
    """Test if two polygons intersect."""
    polygon1 = Polygon(
        (
            (12.492, 41.890),
            (12.492, 41.892),
            (12.494, 41.892),
            (12.494, 41.890),
            (12.492, 41.890),
        )
    )
    polygon2 = Polygon(
        (
            (12.493, 41.891),
            (12.493, 41.893),
            (12.495, 41.893),
            (12.495, 41.891),
            (12.493, 41.891),
        )
    )

    # Create polygons
    poly1 = PolygonData.objects.create(name="Polygon 1", boundary=polygon1)
    poly2 = PolygonData.objects.create(name="Polygon 2", boundary=polygon2)

    # Check if Polygon 2 intersects with Polygon 1
    intersecting_polygons = PolygonData.objects.filter(boundary__intersects=polygon2)

    assert intersecting_polygons.count() == 2
    assert poly1 in intersecting_polygons
    assert poly2 in intersecting_polygons
