import os
import uuid

def poly_fill_xml(label, assetpath, svg_uuid=uuid.uuid4(), fill_uuid=uuid.uuid4()):
    template = f"""    <symbol alpha="1" clip_to_extent="1" force_rhr="0" frame_rate="10" is_animated="0" name="{label}" tags="Geonest Mapping" type="fill">
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
          <Option name="outline_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
          <Option name="outline_style" type="QString" value="solid"/>
          <Option name="outline_width" type="QString" value="0.26"/>
          <Option name="outline_width_unit" type="QString" value="Pixel"/>
          <Option name="style" type="QString" value="solid"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties" type="Map">
              <Option name="fillColor" type="Map">
                <Option name="active" type="bool" value="true"/>
                <Option name="expression" type="QString" value="'#' + upper(geomaplib_to_hex(floor(coalesce(&quot;fill-opacity&quot;, 0) * 255), 2)) + substr(&quot;fill&quot;, 2, 2) +  substr(&quot;fill&quot;, 4, 2) +  substr(&quot;fill&quot;, 6, 2)"/>
                <Option name="type" type="int" value="3"/>
              </Option>
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
      <layer class="SVGFill" enabled="1" id="{{{svg_uuid}}}" locked="0" pass="0">
        <Option type="Map">
          <Option name="angle" type="QString" value="0"/>
          <Option name="color" type="QString" value="0,0,255,255,rgb:0,0,1,1"/>
          <Option name="outline_color" type="QString" value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1"/>
          <Option name="outline_width" type="QString" value="0.26"/>
          <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="outline_width_unit" type="QString" value="MM"/>
          <Option name="parameters"/>
          <Option name="pattern_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="pattern_width_unit" type="QString" value="MM"/>
          <Option name="svgFile" type="QString" value="{assetpath}"/>
          <Option name="svg_outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="svg_outline_width_unit" type="QString" value="MM"/>
          <Option name="width" type="QString" value="8"/>
        </Option>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties" type="Map">
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
    </symbol>\n"""
    return template

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    repo_dir = os.path.realpath(os.path.join(script_dir, '..'))
    main_dir = os.path.join(repo_dir, 'polygon_patterns');
    categories = os.listdir(path=main_dir)
    subcategory_map = {}
    for category in categories:
        sub_dir_path = os.path.realpath(os.path.join(main_dir, category))
        subcategory_map[category] = sub_dir_path

    asset_list = {}
    for category, subdirpath in subcategory_map.items():
        filenames = [item for item in os.listdir(subdirpath) if
                 item.endswith('svg')]
        for filename in filenames:
            label = category + ':' + filename.replace('.svg', '')
            asset_list[label] = os.path.realpath(os.path.join(subdirpath, filename))

    outputfile_path = os.path.realpath(
            os.path.join(repo_dir, 'Geonest-Mapping-Polygon-Pattern-Style.xml'))

    with open(outputfile_path, "w") as we:
        we.write("""<!DOCTYPE qgis_style>\n""")
        we.write("""<qgis_style version="2">\n""")
        we.write("""  <symbols>\n""")
        for label, filepath in asset_list.items():
            assetpath = filepath.replace(repo_dir, '')
            if (assetpath.startswith('/')):
                assetpath = assetpath[1:]
            lexml = poly_fill_xml(label=label, assetpath=assetpath,
                                  svg_uuid=uuid.uuid4(), fill_uuid=uuid.uuid4())
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
