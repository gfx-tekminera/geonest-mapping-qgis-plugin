# Geonest Mapping QGIS Plugin

## Load marker, line, and fill styles on install

### To apply style on geonest mapping geojson file

#### Placemark
- symbology `categorized`
- select `_placemark_type` field, classify
- advanced -> match to saved symbol

#### Line
- symbology `categorized`
- select '_geomap_type' field, classify
- advanced -> match to saved symbol
- change to `rule-based`
- refine `drawing_line` into categories
- select `lineIcon` field, classify
- advanced -> match to saved symbol

#### Polygon
- symbology `categorized`
- select `fill-pattern` field, classify
- advanced -> match to saved symbol
note: 'Pattern00' is default empty polygon fill
