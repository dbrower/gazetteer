
# Data Source

Administrative and country shape files are from [http://www.gadm.org/](); it uses the WGS84 datum.
Coordinates for place names are overlaid from the NGA fact sheets [http://earth-info.nga.mil/gns/html/]().


# Shapefiles

The shapefile spec is at [http://www.esri.com/library/whitepapers/pdfs/shapefile.pdf]().

# python install

Use python to process the data files, and to generate centroids for all the regions.

    brew install geos
    brew install gdal
    pip install shapely
    pip install fiona

http://toblerity.github.io/shapely/manual.html#cascading-unions
http://macwright.org/2012/10/31/gis-with-python-shapely-fiona.html

