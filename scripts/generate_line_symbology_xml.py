import os
import uuid

def line_xml(plugin_dir):
    template = f"""    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="drawing_line" tags="Geonest Mapping" type="line">
      <data_defined_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties"/>
          <Option name="type" type="QString" value="collection"/>
        </Option>
      </data_defined_properties>
      <layer class="SimpleLine" enabled="1" id="{{{uuid.uuid4()}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="align_dash_pattern" type="QString" value="0"/>
          <Option name="capstyle" type="QString" value="square"/>
          <Option name="customdash" type="QString" value="5;2"/>
          <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="customdash_unit" type="QString" value="MM"/>
          <Option name="dash_pattern_offset" type="QString" value="0"/>
          <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
          <Option name="draw_inside_polygon" type="QString" value="0"/>
          <Option name="joinstyle" type="QString" value="bevel"/>
          <Option name="line_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
          <Option name="line_style" type="QString" value="solid"/>
          <Option name="line_width" type="QString" value="4"/>
          <Option name="line_width_unit" type="QString" value="Pixel"/>
          <Option name="offset" type="QString" value="0"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="ring_filter" type="QString" value="0"/>
          <Option name="trim_distance_end" type="QString" value="0"/>
          <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="trim_distance_end_unit" type="QString" value="MM"/>
          <Option name="trim_distance_start" type="QString" value="0"/>
          <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="trim_distance_start_unit" type="QString" value="MM"/>
          <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
          <Option name="use_custom_dash" type="QString" value="0"/>
          <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties" type="Map">
              <Option name="outlineColor" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="'#' + upper(geomaplib_to_hex(floor(coalesce(&quot;stroke-opacity&quot;, 0) * 255), 2)) + substr(&quot;stroke&quot;, 2, 2) +  substr(&quot;stroke&quot;, 4, 2) +  substr(&quot;stroke&quot;, 6, 2)"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="outlineStyle" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="if(&quot;lineStyle&quot; = 1, 'dot', if(&quot;lineStyle&quot; = 2, 'dash', 'solid'))"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="outlineWidth" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;stroke-width&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
            </Option>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
      </layer>
      <layer class="MarkerLine" enabled="1" id="{{{uuid.uuid4()}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="average_angle_length" type="QString" value="4"/>
          <Option name="average_angle_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="average_angle_unit" type="QString" value="MM"/>
          <Option name="blank_segments_unit" type="QString" value="MapUnit"/>
          <Option name="interval" type="QString" value="3"/>
          <Option name="interval_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="interval_unit" type="QString" value="MM"/>
          <Option name="offset" type="QString" value="0"/>
          <Option name="offset_along_line" type="QString" value="0"/>
          <Option name="offset_along_line_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_along_line_unit" type="QString" value="MM"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="place_on_every_part" type="bool" value="true"/>
          <Option name="placements" type="QString" value="Interval"/>
          <Option name="ring_filter" type="QString" value="0"/>
          <Option name="rotate" type="QString" value="1"/>
          <Option name="trim_distance_end" type="QString" value="0"/>
          <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="trim_distance_end_unit" type="QString" value="MM"/>
          <Option name="trim_distance_start" type="QString" value="0"/>
          <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="trim_distance_start_unit" type="QString" value="MM"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="@drawing_line@1" type="marker">
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <layer class="RasterMarker" enabled="1" id="{{{uuid.uuid4()}}}" locked="0" pass="0">
            <Option type="Map">
              <Option name="alpha" type="QString" value="1"/>
              <Option name="angle" type="QString" value="0"/>
              <Option name="fixedAspectRatio" type="QString" value="0"/>
              <Option name="horizontal_anchor_point" type="QString" value="1"/>
              <Option name="imageFile" type="QString" value="{plugin_dir}/line_symbols/anticline.png"/>
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
                  <Option name="name" type="Map">
                    <Option name="active" type="bool" value="true"/>
                    <Option name="expression" type="QString" value="'{plugin_dir}/line_symbols/'|| &quot;lineIcon&quot; ||'.png'"/>
                    <Option name="type" type="int" value="3"/>
                  </Option>
                </Option>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </layer>
    </symbol>
    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="route" tags="Geonest Mapping" type="line">
      <data_defined_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties"/>
          <Option name="type" type="QString" value="collection"/>
        </Option>
      </data_defined_properties>
      <layer class="SimpleLine" enabled="1" id="{{{uuid.uuid4()}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="align_dash_pattern" type="QString" value="0"/>
          <Option name="capstyle" type="QString" value="square"/>
          <Option name="customdash" type="QString" value="5;2"/>
          <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="customdash_unit" type="QString" value="MM"/>
          <Option name="dash_pattern_offset" type="QString" value="0"/>
          <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
          <Option name="draw_inside_polygon" type="QString" value="0"/>
          <Option name="joinstyle" type="QString" value="bevel"/>
          <Option name="line_color" type="QString" value="255,0,0,255,hsv:0,1,1,1"/>
          <Option name="line_style" type="QString" value="solid"/>
          <Option name="line_width" type="QString" value="4"/>
          <Option name="line_width_unit" type="QString" value="Pixel"/>
          <Option name="offset" type="QString" value="0"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="ring_filter" type="QString" value="0"/>
          <Option name="trim_distance_end" type="QString" value="0"/>
          <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="trim_distance_end_unit" type="QString" value="MM"/>
          <Option name="trim_distance_start" type="QString" value="0"/>
          <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="trim_distance_start_unit" type="QString" value="MM"/>
          <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
          <Option name="use_custom_dash" type="QString" value="0"/>
          <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties" type="Map">
              <Option name="outlineColor" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="'#' + upper(geomaplib_to_hex(floor(coalesce(&quot;stroke-opacity&quot;, 0) * 255), 2)) + substr(&quot;stroke&quot;, 2, 2) +  substr(&quot;stroke&quot;, 4, 2) +  substr(&quot;stroke&quot;, 6, 2)"/>
                <Option name="type" type="int" value="3"/>
              </Option>
              <Option name="outlineWidth" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;stroke-width&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
            </Option>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
      </layer>
      <layer class="SimpleLine" enabled="1" id="{{{uuid.uuid4()}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="align_dash_pattern" type="QString" value="0"/>
          <Option name="capstyle" type="QString" value="square"/>
          <Option name="customdash" type="QString" value="2;4"/>
          <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="customdash_unit" type="QString" value="MM"/>
          <Option name="dash_pattern_offset" type="QString" value="0"/>
          <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
          <Option name="draw_inside_polygon" type="QString" value="0"/>
          <Option name="joinstyle" type="QString" value="bevel"/>
          <Option name="line_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
          <Option name="line_style" type="QString" value="dot"/>
          <Option name="line_width" type="QString" value="2"/>
          <Option name="line_width_unit" type="QString" value="Pixel"/>
          <Option name="offset" type="QString" value="0"/>
          <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="ring_filter" type="QString" value="0"/>
          <Option name="trim_distance_end" type="QString" value="0"/>
          <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="trim_distance_end_unit" type="QString" value="MM"/>
          <Option name="trim_distance_start" type="QString" value="0"/>
          <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="trim_distance_start_unit" type="QString" value="MM"/>
          <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
          <Option name="use_custom_dash" type="QString" value="1"/>
          <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
      </layer>
    </symbol>\n"""
    return template

def create_linestyle_xml(plugin_dir):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    repo_dir = os.path.realpath(os.path.join(script_dir, '..'))

    outputfile_path = os.path.realpath(
            os.path.join(repo_dir, 'Geonest-Mapping-Line-Style.xml'))

    with open(outputfile_path, "w") as we:
        we.write("""<!DOCTYPE qgis_style>\n""")
        we.write("""<qgis_style version="2">\n""")
        we.write("""  <symbols>\n""")
        le_plugin_dir = plugin_dir
        if le_plugin_dir.endswith('/'):
          le_plugin_dir = le_plugin_dir[:-1]
        lexml = line_xml(le_plugin_dir)
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
