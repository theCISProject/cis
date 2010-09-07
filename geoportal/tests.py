from django.contrib.gis.db import models
from django.template import Template, TemplateSyntaxError, Context
from django.test import TestCase

import geoportal


BASE_TEMPLATE = """
{%% load geoportal_tags %%}
{%% geoportal_map geo_field %s %%}
"""

JS_TEMPLATE = """
{% load geoportal_tags %}
{% geoportal_js %}
"""

KML_TEMPLATE = """
{%% load geoportal_tags %%}
{%% geoportal_map geo_field as var_name %%}
{%% geoportal_kml var_name %s %%}
"""

GPX_TEMPLATE = """
{%% load geoportal_tags %%}
{%% geoportal_map geo_field as var_name %%}
{%% geoportal_gpx var_name %s %%}
"""


class GeoportalUtilsTest(TestCase):

    def test_utils(self):
        self.assertEquals(len(geoportal.utils.LAYERS), 12)

    def test_get_layers(self):
        layers = (('maps', 1),)
        geo_layers = geoportal.utils.get_layers(layers)
        self.assertEquals(len(geo_layers), 1)
        self.assertEquals(geo_layers[0]['resource_name'],
                          'GEOGRAPHICALGRIDSYSTEMS.MAPS')

        layers = (('photos', 1), ('maps', 0.3))
        geo_layers = geoportal.utils.get_layers(layers)
        self.assertEquals(len(geo_layers), 2)
        self.assertEquals(geo_layers[0]['resource_name'],
                          'ORTHOIMAGERY.ORTHOPHOTOS')


class TestModel(models.Model):
    """A model which is not in the DB but we can use it in our templatetags"""
    point = models.PointField()
    line = models.LineStringField()
    polygon = models.PolygonField()


class GeoTemplateTest(TestCase):

    def setUp(self):
        self.geo_model = TestModel(
            point='POINT (6.8643511274086046 45.8325858329590829)',
            line='LINESTRING (-4.8687808591351045 48.5177935040483490, ' + \
                             '-3.9600705509226786 48.7201659712547794, ' + \
                             '-3.6126224919002792 48.6833709772172654)',
            polygon='POLYGON((1.1981967868713883 48.59138349212341,' + \
                             '1.331830655726157 46.714838796209094,' + \
                             '6.062469613184964 46.64124880813403,' + \
                             '4.9666718885758625 48.70176847423602,' + \
                             '1.1981967868713883 48.59138349212341))',
        )

    def tearDown(self):
        pass

    def test_simple_template(self):
        context = Context({'geo_field': self.geo_model.point})
        rendered = Template(BASE_TEMPLATE % '').render(context)
        self.assertTrue(str(self.geo_model.point) in rendered)

    def test_template_with_options(self):
        context = Context({'geo_field': self.geo_model.line})
        tmpl = Template(BASE_TEMPLATE % 'width=120, height=150')
        self.assertTrue(str(self.geo_model.line) in tmpl.render(context))

    def test_invalid_template(self):
        self.assertRaises(TemplateSyntaxError,
                lambda: Template(BASE_TEMPLATE % 'some_option=some_value').render(Context()))

        self.assertRaises(TemplateSyntaxError,
                lambda: Template(KML_TEMPLATE % '').render(Context()))

        self.assertRaises(TemplateSyntaxError,
                lambda: Template(GPX_TEMPLATE % '').render(Context()))

    def test_template_with_variable(self):
        context = Context({'geo_field': self.geo_model.polygon,
                           'map_width': 200,
                           'map_height': 400})
        template_str = BASE_TEMPLATE % 'width=map_width, height=map_height'
        rendered = Template(template_str).render(context)
        self.assertTrue('width: 200px; height: 400px;' in rendered)
        self.assertTrue(str(self.geo_model.polygon) in rendered)

    def test_invisible_feature(self):
        context = Context({'geo_field': self.geo_model.polygon})
        rendered = Template(BASE_TEMPLATE % 'visible=0').render(context)
        # This is the line that sets the feature as invisible
        self.assertTrue('visibility: false' in rendered)

    def test_as_var_name(self):
        context = Context({'geo_field': self.geo_model.polygon})
        rendered = Template(BASE_TEMPLATE % 'as some_variable').render(context)

        # This is 'map_' +  a 5-char random string
        self.assertEquals(len(context['some_variable']), 9)

    def test_javascript_tag(self):
        rendered = Template(JS_TEMPLATE).render(Context({}))
        self.assertTrue('<script type="text/javascript" src="' in rendered)

    def test_kml(self):
        context = Context({'geo_field': self.geo_model.polygon})
        rendered = Template(KML_TEMPLATE % '/kml_url.kml').render(context)
        self.assertTrue('kml.extract = true;' in rendered)
        self.assertTrue('new OpenLayers.Format.KML' in rendered)
        self.assertTrue("url: '/kml_url.kml'," in rendered)
        self.assertTrue("viewer.map.zoomToExtent(bounds);" in rendered)
        self.assertTrue("new OpenLayers.Popup.FramedCloud" in rendered)

        tmpl = Template(KML_TEMPLATE % '/kml_url.kml width=5')
        rendered = tmpl.render(context)
        self.assertTrue('kml.extract = false;' in rendered)

        tmpl = Template(KML_TEMPLATE % '/kml_url.kml focus=0')
        rendered = tmpl.render(context)
        self.assertFalse("viewer.map.zoomToExtent(bounds);" in rendered)

        tmpl = Template(KML_TEMPLATE % '/kml_url.kml popup=0')
        rendered = tmpl.render(context)
        self.assertFalse("new OpenLayers.Popup.FramedCloud" in rendered)

    def test_gpx(self):
        context = Context({'geo_field': self.geo_model.polygon})
        rendered = Template(GPX_TEMPLATE % '/gpx_url.gpx').render(context)
        self.assertTrue('gpx.extract = true;' in rendered)
        self.assertTrue('new OpenLayers.Format.GPX' in rendered)
        self.assertTrue("url: '/gpx_url.gpx'," in rendered)
        self.assertTrue("viewer.map.zoomToExtent(bounds);" in rendered)
        self.assertTrue("new OpenLayers.Popup.FramedCloud" in rendered)

        tmpl = Template(GPX_TEMPLATE % '/gpx_url.gpx opacity=0.7')
        rendered = tmpl.render(context)
        self.assertTrue('gpx.extract = true;' in rendered)

        tmpl = Template(GPX_TEMPLATE % '/gpx_url.gpx focus=0')
        rendered = tmpl.render(context)
        self.assertFalse("viewer.map.zoomToExtent(bounds);" in rendered)

        tmpl = Template(GPX_TEMPLATE % '/gpx_url.gpx popup=0')
        rendered = tmpl.render(context)
        self.assertFalse("new OpenLayers.Popup.FramedCloud" in rendered)


class TestForm(geoportal.forms.Form):
    name = geoportal.forms.CharField(max_length=255)
    point = geoportal.forms.PointField()


class CustomForm(geoportal.forms.Form):
    """ Lots of overriden attributes """
    multipolygon = geoportal.forms.MultiPolygonField(
        widget=geoportal.forms.MultiPolygonWidget(attrs={
            'width': 300,
            'height': 350,
            'color': 'eeccaa',
            'opacity': 0.1,
            'srid': 900913,
            'layers': (('photos', 1),),
        },
    ))


class FormsTests(TestCase):

    def test_field(self):
        form = TestForm(data={
            'name': 'Testing',
            'point': 'SRID=4326;POINT(3.363065462318639 46.44807508943696)',
        })
        self.assertTrue(form.is_valid())

    def test_widget(self):
        form = TestForm()
        for field in form:
            if field.name == 'point':
                fld = '%s' % field
                self.assertTrue('point.is_point = true;' in fld)
                self.assertTrue('point.is_collection = false;' in fld)

    def test_custom_widget(self):
        form = CustomForm()
        for field in form:
            fld = '%s' % field
            self.assertTrue('multipolygon.is_point = false;' in fld)
            self.assertTrue('multipolygon.is_collection = true;' in fld)
            self.assertTrue('multipolygon.is_polygon = true;' in fld)
            self.assertTrue('style="width: 300px; height: 350px;"' in fld)
            self.assertTrue('EPSG:900913' in fld)
            self.assertTrue("strokeColor: '#eeccaa'" in fld)
            self.assertTrue('fillOpacity: 0.1,' in fld)
            self.assertTrue('ORTHOIMAGERY.ORTHOPHOTOS:WMSC' in fld)
