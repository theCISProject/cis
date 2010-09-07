from django.contrib.gis.forms.fields import GeometryField
from geoportal.forms import widgets


class PointField(GeometryField):
    widget = widgets.PointWidget


class MultiPointField(GeometryField):
    widget = widgets.MultiPointWidget


class LineStringField(GeometryField):
    widget = widgets.LineStringWidget


class MultiLineStringField(GeometryField):
    widget = widgets.MultiLineStringWidget


class PolygonField(GeometryField):
    widget = widgets.PolygonWidget


class MultiPolygonField(GeometryField):
    widget = widgets.MultiPolygonWidget
