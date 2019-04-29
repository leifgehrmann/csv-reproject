# csv-reproject

A command line tool to reproject a CSV from one Coordinate Reference System to
another.

## Example

Imagine the following CSV file with some annoying columns:

```
Id,Name,Easting/Northing
10,Bob," 325311,673501"
20,Alice," 259562,664497"
30,Carol," 266645,845032"
```

To re-project these coordinates, one can run the following command:

```
csv-reproject \
    --from-proj="epsg:27700" \
    --from-x-column="Easting/Northing" \
    --from-x-format=" (-?[0-9.]+),.*" \
    --from-y-column="Easting/Northing" \
    --from-y-format=".*,(-?[0-9.]+)" \
    --to-proj="EPSG:4326" \
    --to-x-header=Longitude \
    --to-y-header=Latitude \
    myData.csv
```

This will modify the file to have two new columns called `Longitude` and
`Latitude` which can now easily be imported into software like JOSM!
