import os
import uuid

def marker_pattern_xml(label, assetpath, marker_uuid, bg_uuid, svg_uuid):
    template = f"""    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="{label}" tags="Geonest Mapping" type="marker">
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
        <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="@{label}@0" type="fill">
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
              <Option name="svgFile" type="QString" value="{assetpath}"/>
              <Option name="svg_outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="svg_outline_width_unit" type="QString" value="MM"/>
              <Option name="width" type="QString" value="6"/>
            </Option>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </layer>
    </symbol>"""
    return template

def marker_structure_xml(label, assetpath, svg_uuid):
    template = f"""    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="{label}" tags="Geonest Mapping" type="marker">
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
          <Option name="name" type="QString" value="{assetpath}"/>
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
    </symbol>"""
    return template

def marker_general_xml(label, assetpath, svg_uuid):
    template = f"""    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="{label}" tags="Geonest Mapping" type="marker">
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
          <Option name="name" type="QString" value="{assetpath}"/>
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
              <Option name="fillColor" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="&quot;marker-color&quot;"/>
                <Option name="type" type="int" value="3"/>
              </Option>
            </Option>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
      </layer>
    </symbol>"""
    return template

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    repo_dir = os.path.realpath(os.path.join(script_dir, '..'))
    symbol1_dir = os.path.join(repo_dir, 'placemark_symbols');
    symbol2_dir = os.path.join(repo_dir, 'polygon_patterns');

    outputfile_path = os.path.realpath(
            os.path.join(repo_dir, 'Geonest-Mapping-Marker-Style.xml'))

    with open(outputfile_path, "w") as we:
        we.write("""<!DOCTYPE qgis_style>\n""")
        we.write("""<qgis_style version="2">\n""")
        we.write("""  <symbols>\n""")
        lithologies = os.listdir(path=symbol2_dir)
        for lithology in lithologies:
            lithodir_path = os.path.realpath(os.path.join(symbol2_dir, lithology))
            filenames = [item for item in os.listdir(lithodir_path) if
                         item.endswith('svg')]
            for filename in filenames:
                label = lithology + ':' + filename.replace('.svg', '')
                assetpath = os.path.realpath(os.path.join(lithodir_path, filename))
                assetpath = assetpath.replace(repo_dir, '')
                if (assetpath.startswith('/')):
                    assetpath = assetpath[1:]
                lexml = marker_pattern_xml(label=label, assetpath=assetpath,
                                           marker_uuid=uuid.uuid4(),
                                           bg_uuid=uuid.uuid4(),
                                           svg_uuid=uuid.uuid4())
                we.write(lexml)

        makidir_path = os.path.realpath(os.path.join(symbol1_dir, 'mapbox-maki'))
        makiicons = [item for item in os.listdir(makidir_path) if
                     item.endswith('svg')]
        for filename in makiicons:
            label = filename.replace('.svg', '')
            assetpath = os.path.realpath(os.path.join(makidir_path, filename))
            assetpath = assetpath.replace(repo_dir, '')
            if assetpath.startswith('/'):
                assetpath = assetpath[1:]
            lexml = marker_general_xml(label=label, assetpath=assetpath,
                                       svg_uuid=uuid.uuid4())
            we.write(lexml)

        geomaplibdir_path = os.path.realpath(os.path.join(symbol1_dir, 'geomaplib'))
        geomaplibicons = [item for item in os.listdir(geomaplibdir_path) if
                          item.endswith('svg')]
        for filename in geomaplibicons:
            label = filename.replace('.svg', '')
            assetpath = os.path.realpath(os.path.join(geomaplibdir_path, filename))
            assetpath = assetpath.replace(repo_dir, '')
            if assetpath.startswith('/'):
                assetpath = assetpath[1:]
            lexml = marker_structure_xml(label=label, assetpath=assetpath,
                                         svg_uuid=uuid.uuid4())
            we.write(lexml)

        we.write("""  </symbols>\n""")
        we.write("""  <colorramps/>\n""")
        we.write("""  <textformats/>\n""")
        we.write("""  <labelsettings/>\n""")
        we.write("""  <legendpatchshapes/>\n""")
        we.write("""  <symbols3d/>\n""")
        we.write("""  <materialsettings/>\n""")
        we.write("""</qgis_style>""")

main()
