import click
from pyproj import Proj, transform

from csv_reproject import CsvProjReader, CsvProjWriter


@click.command()
@click.option('--from-proj', default='EPSG:4326',
              help='The projection to convert from.')
@click.option('--from-x-column', default='X',
              help='The column name of the X value to project from.')
@click.option('--from-y-column', default='Y',
              help='The column name of the Y value to project from.')
@click.option('--from-x-format', default='(-?[0-9.]+)',
              help='The pattern to search for in the X column.')
@click.option('--from-y-format', default='(-?[0-9.]+)',
              help='The pattern to search for in the Y column.')
@click.option('--to-proj', default='EPSG:4326',
              help='The projection to convert to.')
@click.option('--to-x-header', default='X',
              help='The column name to store the reprojected X value.')
@click.option('--to-y-header', default='Y',
              help='The column name to store the reprojected Y value.')
@click.argument('input-filename')
@click.argument('output-filename')
def cli(
        from_proj: str,
        from_x_column: str,
        from_y_column: str,
        from_x_format: str,
        from_y_format: str,
        to_proj: str,
        to_x_header: str,
        to_y_header: str,
        input_filename: str,
        output_filename: str
):
    """Reproject a CSV from one Coordinate Reference System to another."""

    from_proj = Proj(init=from_proj)
    to_proj = Proj(init=to_proj)

    with open(input_filename) as input_file, \
            open(output_filename, 'w') as output_file:

        reader = CsvProjReader(
            input_file,
            from_x_column,
            from_y_column,
            from_x_format,
            from_y_format
        )

        writer = CsvProjWriter(
            output_file,
            to_x_header,
            to_y_header
        )

        input_headers = reader.read_headers()
        writer.write_headers(input_headers)

        for csv_proj_row in reader.read_proj_rows():
            new_x, new_y = [None, None]
            if csv_proj_row.x is not None and csv_proj_row.x is not None:
                new_x, new_y = transform(
                    from_proj,
                    to_proj,
                    csv_proj_row.x,
                    csv_proj_row.y
                )
            writer.write_row(csv_proj_row.row, new_x, new_y)


if __name__ == '__main__':
    cli()
