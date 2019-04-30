test-example:
	./csv-reproject \
	--from-proj="epsg:27700" \
	--from-x-column="Easting/Northing" \
	--from-x-format=" (-?[0-9.]+),.*" \
	--from-y-column="Easting/Northing" \
	--from-y-format=".*,(-?[0-9.]+)" \
	--to-proj="EPSG:4326" \
	--to-x-header=Longitude \
	--to-y-header=Latitude \
	example/myData.csv \
	example/myData-transformed.csv
