import os
import uuid

def marker_lithology_xml(lithology_dir, marker_uuid, bg_uuid, svg_uuid):
    template = f"""    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="lithology" tags="Geonest Mapping" type="marker">
      <data_defined_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties"/>
          <Option name="type" type="QString" value="collection"/>
        </Option>
      </data_defined_properties>
      <layer class="FilledMarker" enabled="1" id="{{{marker_uuid}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="angle" type="QString" value="0"/>
          <Option name="color" type="QString" value="255,255,255,255,hsv:1,0,1,1"/>
          <Option name="horizontal_anchor_point" type="QString" value="1"/>
          <Option name="name" type="QString" value="circle"/>
          <Option name="offset" type="QString" value="0,0"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="scale_method" type="QString" value="diameter"/>
          <Option name="size" type="QString" value="6"/>
          <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="size_unit" type="QString" value="MM"/>
          <Option name="vertical_anchor_point" type="QString" value="1"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="@lithology@0" type="fill">
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <layer class="SimpleFill" enabled="1" id="{{{bg_uuid}}}" locked="0" pass="0">
            <Option type="Map">
              <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="color" type="QString" value="255,255,255,255,hsv:1,0,1,1"/>
              <Option name="joinstyle" type="QString" value="bevel"/>
              <Option name="offset" type="QString" value="0,0"/>
              <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offset_unit" type="QString" value="MM"/>
              <Option name="outline_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
              <Option name="outline_style" type="QString" value="solid"/>
              <Option name="outline_width" type="QString" value="0.26"/>
              <Option name="outline_width_unit" type="QString" value="MM"/>
              <Option name="style" type="QString" value="solid"/>
            </Option>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
          <layer class="SVGFill" enabled="1" id="{{{svg_uuid}}}" locked="0" pass="0">
            <Option type="Map">
              <Option name="angle" type="QString" value="0"/>
              <Option name="color" type="QString" value="255,255,255,255,hsv:1,0,1,1"/>
              <Option name="outline_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
              <Option name="outline_width" type="QString" value="0"/>
              <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="outline_width_unit" type="QString" value="MM"/>
              <Option name="parameters"/>
              <Option name="pattern_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="pattern_width_unit" type="QString" value="MM"/>
              <Option name="svgFile" type="QString" value="polygon_patterns/igneous/banded.svg"/>
              <Option name="svg_outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="svg_outline_width_unit" type="QString" value="MM"/>
              <Option name="width" type="QString" value="6"/>
            </Option>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties" type="Map">
                  <Option name="file" type="Map">
                    <Option name="active" type="bool" value="true"/>
                    <Option name="expression" type="QString" value="'{lithology_dir}/'|| string_to_array(&quot;marker-symbol&quot;, ':')[0] ||'/'|| string_to_array(&quot;marker-symbol&quot;, ':')[1] ||'.svg'"/>
                    <Option name="type" type="int" value="3"/>
                  </Option>
                </Option>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </layer>
    </symbol>\n"""
    return template

def marker_structure_xml(structure_dir, svg_uuid, dip_uuid):
    template = f"""    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="structure" tags="Geonest Mapping" type="marker">
      <data_defined_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties"/>
          <Option name="type" type="QString" value="collection"/>
        </Option>
      </data_defined_properties>
      <layer class="SvgMarker" enabled="1" id="{{{svg_uuid}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="angle" type="QString" value="0"/>
          <Option name="color" type="QString" value="0,0,0,255,rgb:0,0,0,1"/>
          <Option name="fixedAspectRatio" type="QString" value="0"/>
          <Option name="horizontal_anchor_point" type="QString" value="1"/>
          <Option name="name" type="QString" value="placemark_symbols/geomaplib/vertical-bedding-2.svg"/>
          <Option name="offset" type="QString" value="-0.19999999999999987,-0.19999999999999987"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="outline_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
          <Option name="outline_width" type="QString" value="0"/>
          <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="outline_width_unit" type="QString" value="MM"/>
          <Option name="parameters"/>
          <Option name="scale_method" type="QString" value="diameter"/>
          <Option name="size" type="QString" value="8"/>
          <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="size_unit" type="QString" value="MM"/>
          <Option name="vertical_anchor_point" type="QString" value="1"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties" type="Map">
              <Option name="angle" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;strike&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="fillColor" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;marker-color&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="name" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="'{structure_dir}/'|| &quot;marker-symbol&quot; ||'.svg'"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="outlineColor" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;marker-color&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
            </Option>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
      </layer>
      <layer class="FontMarker" enabled="1" id="{{{dip_uuid}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="angle" type="QString" value="0"/>
          <Option name="chr" type="QString" value="90"/>
          <Option name="color" type="QString" value="0,0,0,255,hsv:0,0,0,1"/>
          <Option name="font" type="QString" value="FreeMono"/>
          <Option name="font_style" type="QString" value="Bold"/>
          <Option name="horizontal_anchor_point" type="QString" value="1"/>
          <Option name="joinstyle" type="QString" value="bevel"/>
          <Option name="offset" type="QString" value="3.40000000000000036,-1.79999999999999982"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="outline_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
          <Option name="outline_width" type="QString" value="0"/>
          <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="outline_width_unit" type="QString" value="MM"/>
          <Option name="size" type="QString" value="2.4"/>
          <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="size_unit" type="QString" value="MM"/>
          <Option name="vertical_anchor_point" type="QString" value="1"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties" type="Map">
              <Option name="angle" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;strike&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="char" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;dip&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
            </Option>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
      </layer>
    </symbol>\n"""
    return template

def marker_general_xml(general_dir, lithology_dir, marker_uuid, fmarker_uuid,
                       fill_uuid, svg_uuid):
    template = f"""    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="general" tags="Geonest Mapping" type="marker">
      <data_defined_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties"/>
          <Option name="type" type="QString" value="collection"/>
        </Option>
      </data_defined_properties>
      <layer class="SvgMarker" enabled="1" id="{{{marker_uuid}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="angle" type="QString" value="0"/>
          <Option name="color" type="QString" value="0,0,0,255,rgb:0,0,0,1"/>
          <Option name="fixedAspectRatio" type="QString" value="0"/>
          <Option name="horizontal_anchor_point" type="QString" value="1"/>
          <Option name="name" type="QString" value="placemark_symbols/mapbox-maki/circle.svg"/>
          <Option name="offset" type="QString" value="-0.14999999999999986,-0.14999999999999986"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="outline_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
          <Option name="outline_width" type="QString" value="0"/>
          <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="outline_width_unit" type="QString" value="MM"/>
          <Option name="parameters"/>
          <Option name="scale_method" type="QString" value="diameter"/>
          <Option name="size" type="QString" value="8"/>
          <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="size_unit" type="QString" value="MM"/>
          <Option name="vertical_anchor_point" type="QString" value="1"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties" type="Map">
              <Option name="fillColor" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;marker-color&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="height" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="if (array_length(string_to_array(&quot;marker-symbol&quot;, ':')) = 1, 8, 0)"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="name" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="'{general_dir}/'|| &quot;marker-symbol&quot; ||'.svg'"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="width" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="if (array_length(string_to_array(&quot;marker-symbol&quot;, ':')) = 1, 8, 0)"/>
                <Option name="type" type="int" value="3"/>
              </Option>
            </Option>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
      </layer>
      <layer class="FilledMarker" enabled="1" id="{{{fmarker_uuid}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="angle" type="QString" value="0"/>
          <Option name="color" type="QString" value="255,255,255,255,hsv:1,0,1,1"/>
          <Option name="horizontal_anchor_point" type="QString" value="1"/>
          <Option name="name" type="QString" value="circle"/>
          <Option name="offset" type="QString" value="0,0"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="scale_method" type="QString" value="diameter"/>
          <Option name="size" type="QString" value="6"/>
          <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="size_unit" type="QString" value="MM"/>
          <Option name="vertical_anchor_point" type="QString" value="1"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties" type="Map">
              <Option name="size" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="if (array_length(string_to_array(&quot;marker-symbol&quot;, ':')) = 1, 0, 6)"/>
                <Option name="type" type="int" value="3"/>
              </Option>
            </Option>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="@general@1" type="fill">
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <layer class="SimpleFill" enabled="1" id="{{{fill_uuid}}}" locked="0" pass="0">
            <Option type="Map">
              <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="color" type="QString" value="255,255,255,255,hsv:1,0,1,1"/>
              <Option name="joinstyle" type="QString" value="bevel"/>
              <Option name="offset" type="QString" value="0,0"/>
              <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offset_unit" type="QString" value="MM"/>
              <Option name="outline_color" type="QString" value="0,0,0,255,hsv:0,0,0,1"/>
              <Option name="outline_style" type="QString" value="solid"/>
              <Option name="outline_width" type="QString" value="0.26"/>
              <Option name="outline_width_unit" type="QString" value="Pixel"/>
              <Option name="style" type="QString" value="solid"/>
            </Option>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
          <layer class="SVGFill" enabled="1" id="{{{svg_uuid}}}" locked="0" pass="0">
            <Option type="Map">
              <Option name="angle" type="QString" value="0"/>
              <Option name="color" type="QString" value="255,255,255,255,rgb:1,1,1,1"/>
              <Option name="data" type="QString" value="3c7376672077696474683d27313027206865696768743d273130273e3c7465787420783d27352720793d2731302720666f6e742d73697a653d2731302720746578742d616e63686f723d276d6964646c65273e3f3c2f746578743e3c2f7376673e"/>
              <Option name="outline_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
              <Option name="outline_width" type="QString" value="0.2"/>
              <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="outline_width_unit" type="QString" value="MM"/>
              <Option name="parameters"/>
              <Option name="pattern_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="pattern_width_unit" type="QString" value="MM"/>
              <Option name="svg_outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="svg_outline_width_unit" type="QString" value="MM"/>
              <Option name="width" type="QString" value="6"/>
            </Option>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties" type="Map">
                  <Option name="file" type="Map">
                    <Option name="active" type="bool" value="true"/>
                    <Option name="expression" type="QString" value="'{lithology_dir}/'|| string_to_array(&quot;marker-symbol&quot;, ':')[0] ||'/'|| string_to_array(&quot;marker-symbol&quot;, ':')[1] ||'.svg'"/>
                    <Option name="type" type="int" value="3"/>
                  </Option>
                  <Option name="fillColor" type="Map">
                    <Option name="active" type="bool" value="false"/>
                    <Option name="type" type="int" value="1"/>
                    <Option name="val" type="QString" value=""/>
                  </Option>
                  <Option name="outlineColor" type="Map">
                    <Option name="active" type="bool" value="false"/>
                    <Option name="type" type="int" value="1"/>
                    <Option name="val" type="QString" value=""/>
                  </Option>
                  <Option name="outlineWidth" type="Map">
                    <Option name="active" type="bool" value="false"/>
                    <Option name="type" type="int" value="1"/>
                    <Option name="val" type="QString" value=""/>
                  </Option>
                </Option>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </layer>
    </symbol>\n"""
    return template

def create_markerstyle_xml(plugin_path):
    repo_dir = os.path.realpath(plugin_path)
    vector_dir = os.path.join(repo_dir, 'placemark_symbols');

    general_dir = os.path.join(vector_dir, 'mapbox-maki');
    structure_dir = os.path.join(vector_dir, 'geomaplib');
    lithology_dir = os.path.join(repo_dir, 'polygon_patterns');

    outputfile_path = os.path.realpath(
            os.path.join(repo_dir, 'Geonest-Mapping-Marker-Style.xml'))

    with open(outputfile_path, "w") as we:
        we.write("""<!DOCTYPE qgis_style>\n""")
        we.write("""<qgis_style version="2">\n""")
        we.write("""  <symbols>\n""")
        lexml = marker_general_xml(general_dir, lithology_dir,
                                   uuid.uuid4(), uuid.uuid4(),
                                   uuid.uuid4(), uuid.uuid4())
        we.write(lexml)
        lexml = marker_structure_xml(structure_dir, uuid.uuid4(), uuid.uuid4())
        we.write(lexml)
        lexml = marker_lithology_xml(lithology_dir, uuid.uuid4(), uuid.uuid4(),
                                     uuid.uuid4())
        we.write(lexml)

        we.write("""  </symbols>\n""")
        we.write("""  <colorramps/>\n""")
        we.write("""  <textformats/>\n""")
        we.write("""  <labelsettings/>\n""")
        we.write("""  <legendpatchshapes/>\n""")
        we.write("""  <symbols3d/>\n""")
        we.write("""  <materialsettings/>\n""")
        we.write("""</qgis_style>""")

        return outputfile_path
