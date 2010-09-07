{% comment %}
Author: Justin Bronn, Travis Pinney & Dane Springmeyer.
Hacked by Bruno Renié to make it work with the Géoportail API.
{% endcomment %}
{% block vars %}var {{ module }} = {};
{{ module }}.map = null; {{ module }}.controls = null; {{ module }}.panel = null; {{ module }}.re = new RegExp("^SRID=\d+;(.+)", "i"); {{ module }}.layers = {};
{{ module }}.wkt_f = new OpenLayers.Format.WKT();
{{ module }}.is_collection = {{ is_collection|yesno:"true,false" }};
{{ module }}.collection_type = '{{ collection_type }}';
{{ module }}.is_linestring = {{ is_linestring|yesno:"true,false" }};
{{ module }}.is_polygon = {{ is_polygon|yesno:"true,false" }};
{{ module }}.is_point = {{ is_point|yesno:"true,false" }};
{% endblock %}
{{ module }}.get_ewkt = function(feat){return 'SRID={{ srid }};' + {{ module }}.wkt_f.write(feat);}
{{ module }}.read_wkt = function(wkt){
  // OpenLayers cannot handle EWKT -- we make sure to strip it out.
  // EWKT is only exposed to OL if there's a validation error in the admin.
  var match = {{ module }}.re.exec(wkt);
  if (match){wkt = match[1];}
  var wkt = {{ module }}.wkt_f.read(wkt);
  wkt = new OpenLayers.Feature.Vector(wkt.geometry.transform(new OpenLayers.Projection('EPSG:{{ srid }}'), {{ module }}.map.getProjection()));
  return wkt;
}
{{ module }}.write_wkt = function(feat){
  if ({{ module }}.is_collection){ {{ module }}.num_geom = feat.geometry.components.length;}
  else { {{ module }}.num_geom = 1;}
  var feat2 = feat.clone();
  var feat_epsg = new OpenLayers.Feature.Vector(feat2.geometry.transform({{ module }}.map.getProjection(), new OpenLayers.Projection('EPSG:{{ srid }}')));
  document.getElementById('{{ id }}').value = {{ module }}.get_ewkt(feat_epsg);
}
{{ module }}.add_wkt = function(event){
  // This function will sync the contents of the `vector` layer with the
  // WKT in the text field.
  if ({{ module }}.is_collection){
    var feat = new OpenLayers.Feature.Vector(new OpenLayers.Geometry.{{ geom_type }}());
    for (var i = 0; i < {{ module }}.layers.vector.features.length; i++){
      feat.geometry.addComponents([{{ module }}.layers.vector.features[i].geometry]);
    }
    {{ module }}.write_wkt(feat);
  } else {
    // Make sure to remove any previously added features.
    if ({{ module }}.layers.vector.features.length > 1){
      old_feats = [{{ module }}.layers.vector.features[0]];
      {{ module }}.layers.vector.removeFeatures(old_feats);
      {{ module }}.layers.vector.destroyFeatures(old_feats);
    }
    {{ module }}.write_wkt(event.feature);
  }
}
{{ module }}.modify_wkt = function(event){
  if ({{ module }}.is_collection){
    if ({{ module }}.is_point){
      {{ module }}.add_wkt(event); 
      return;
    } else {
      // When modifying the selected components are added to the
      // vector layer so we only increment to the `num_geom` value.
      var feat = new OpenLayers.Feature.Vector(new OpenLayers.Geometry.{{ geom_type }}());
      for (var i = 0; i < {{ module }}.num_geom; i++){
	feat.geometry.addComponents([{{ module }}.layers.vector.features[i].geometry]);
      }
      {{ module }}.write_wkt(feat);
    }
  } else {
    {{ module }}.write_wkt(event.feature);
  }
}
// Function to clear vector features and purge wkt from div
{{ module }}.deleteFeatures = function(){
  {{ module }}.layers.vector.removeFeatures({{ module }}.layers.vector.features);
  {{ module }}.layers.vector.destroyFeatures();
}
{{ module }}.clearFeatures = function (){
  {{ module }}.deleteFeatures();
  document.getElementById('{{ id }}').value = '';
  var center = new OpenLayers.LonLat({{ default_lon|escapejs }}, {{ default_lat|escapejs }});
  center = center.transform(new OpenLayers.Projection('EPSG:{{ srid }}'), {{ module }}.map.getProjection());
  {{ module }}.map.setCenter(center, {{ default_zoom }});
}
// Add Select control
{{ module }}.addSelectControl = function(){
  var select = new OpenLayers.Control.SelectFeature({{ module }}.layers.vector, {'toggle' : true, 'clickout' : true});
  viewer_{{ id }}.map.addControl(select);
  select.activate();
}
{{ module }}.enableDrawing = function(){ {{ module }}.map.getControlsByClass('OpenLayers.Control.DrawFeature')[0].activate();}
{{ module }}.enableEditing = function(){ {{ module }}.map.getControlsByClass('OpenLayers.Control.ModifyFeature')[0].activate();}
// Create an array of controls based on geometry type
{{ module }}.getControls = function(lyr){
  {{ module }}.panel = new OpenLayers.Control.Panel({'displayClass': 'olControlEditingToolbar'});
  var nav = new OpenLayers.Control.Navigation();
  var draw_ctl;
  if ({{ module }}.is_linestring){
    draw_ctl = new OpenLayers.Control.DrawFeature(lyr, OpenLayers.Handler.Path, {'displayClass': 'olControlDrawFeaturePath'});
  } else if ({{ module }}.is_polygon){
    draw_ctl = new OpenLayers.Control.DrawFeature(lyr, OpenLayers.Handler.Polygon, {'displayClass': 'olControlDrawFeaturePolygon'});
  } else if ({{ module }}.is_point){
    draw_ctl = new OpenLayers.Control.DrawFeature(lyr, OpenLayers.Handler.Point, {'displayClass': 'olControlDrawFeaturePoint'});
  }
  {% if modifiable %}
  var mod = new OpenLayers.Control.ModifyFeature(lyr, {'displayClass': 'olControlModifyFeature'});
  var drag = new OpenLayers.Control.DragFeature(lyr, {'displayClass': 'olControlDragFeature'});
  {{ module }}.controls = [nav, draw_ctl, mod, drag];
  {% else %}
  {{ module }}.controls = [nav, draw_ctl];
  {% endif %}  
}

{{ module }}.init = function(){
    var options = new Object();
    options.apiKey = '{{ api_key }}';
    options[options.apiKey] = {
      tokenServer:{url:'http://jeton-api.ign.fr',ttl:600},
      tokenTimeOut:600,
      bounds: [-180.0,-90.0,180.0,90.0],
      allowedGeoportalLayers:[],
      resources:{}
    };
    {% for layer in layers %}
    options[options.apiKey].allowedGeoportalLayers.push('{{ layer.name }}');
    options[options.apiKey].resources['{{ layer.name }}'] = {name:'{{ layer.resource_name }}',type:'WMSC',url:'{{ wms_url }}'};
    {% endfor %}
    viewer_{{ id }} = new Geoportal.Viewer.Default("{{ id }}_map", options);
    viewer_{{ id }}.setToolsPanelVisibility(false);
    {% if not map_info %}viewer_{{ id }}.setInformationPanelVisibility(false);{% endif %}
    // Add all the available layers
    {% for layer in layers %}
    viewer_{{ id }}.addGeoportalLayer('{{ layer.name }}', {opacity: {{ layer.opacity }}, name: '{{ layer.switcher_name }}', buffer: 1, transitionEffect: 'resize'});
    {% endfor %}{{ module }}.map = viewer_{{ id }}.map;
    {% if is_linestring %}OpenLayers.Feature.Vector.style["default"]["strokeWidth"] = 3; // Default too thin for linestrings. {% endif %}
    OpenLayers.Feature.Vector.style["default"]["fillOpacity"] = {{ feature_opacity|escapejs }};
    OpenLayers.Feature.Vector.style["default"]["strokeColor"] = "#{{ feature_color }}";
    OpenLayers.Feature.Vector.style["default"]["fillColor"] = "#{{ feature_color }}";
    {{ module }}.layers.vector = new OpenLayers.Layer.Vector(" {{ field_name }}");
    {{ module }}.map.addLayer({{ module }}.layers.vector);
    // Read WKT from the text field.
    var wkt = document.getElementById('{{ id }}').value;
    if (wkt){
      // After reading into geometry, immediately write back to 
      // WKT <textarea> as EWKT (so that SRID is included).
      var admin_geom = {{ module }}.read_wkt(wkt);
      {{ module }}.write_wkt(admin_geom);
      if ({{ module }}.is_collection){
	// If geometry collection, add each component individually so they may be
	// edited individually.
	for (var i = 0; i < {{ module }}.num_geom; i++){
	  {{ module }}.layers.vector.addFeatures([new OpenLayers.Feature.Vector(admin_geom.geometry.components[i].clone())]);
	}
      } else {
	{{ module }}.layers.vector.addFeatures([admin_geom]);
      }
      // Zooming to the bounds - ZOOM 3 TIMES, THAT'S MAGIC
      {{ module }}.map.zoomToExtent(admin_geom.geometry.getBounds());
      {{ module }}.map.zoomToExtent(admin_geom.geometry.getBounds());
      {{ module }}.map.zoomToExtent(admin_geom.geometry.getBounds());
      if ({{ module }}.is_point && !{{ module }}.is_collection){
          {{ module }}.map.zoomTo({{ point_zoom }}); 
      }
    } else {
      var center = new OpenLayers.LonLat({{ default_lon|escapejs }}, {{ default_lat|escapejs }});
      center = center.transform(new OpenLayers.Projection('EPSG:{{ srid }}'), {{ module }}.map.getProjection());
      {{ module }}.map.setCenter(center, {{ default_zoom }});
    }
    // This allows editing of the geographic fields -- the modified WKT is
    // written back to the content field (as EWKT, so that the ORM will know
    // to transform back to original SRID).
    {{ module }}.layers.vector.events.on({"featuremodified" : {{ module }}.modify_wkt});
    {{ module }}.layers.vector.events.on({"featureadded" : {{ module }}.add_wkt});
    {% block controls %}
    // Map controls:
    // Add geometry specific panel of toolbar controls
    {{ module }}.getControls({{ module }}.layers.vector);
    {{ module }}.panel.addControls({{ module }}.controls);
    {{ module }}.map.addControl({{ module }}.panel);
    {{ module }}.addSelectControl();
    // Then add optional visual controls
    {% if mouse_position %}{{ module }}.map.addControl(new OpenLayers.Control.MousePosition());{% endif %}
    {% if scale_text %}{{ module }}.map.addControl(new OpenLayers.Control.Scale());{% endif %}
    {% if layerswitcher %}{{ module }}.map.addControl(new OpenLayers.Control.LayerSwitcher());{% else %}
    viewer_{{ id }}.setLayersPanelVisibility(false);{% endif %}
    // Then add optional behavior controls
    {{ module }}.map.addControl(new OpenLayers.Control.PanZoomBar());
    {% if not scrollable %}{{ module }}.map.getControlsByClass('OpenLayers.Control.Navigation')[0].disableZoomWheel();{% endif %}
    {% endblock %}
    if (wkt){
      {{ module }}.enableEditing();
    } else {
      {{ module }}.enableDrawing();
    }
}
