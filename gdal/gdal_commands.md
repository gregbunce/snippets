gdal command cheatsheet

#### shapefile to geojson
ogr2ogr -f GeoJSON -t_srs crs:84 C:\\temp\output.geojson C:\\temp\input.shp
