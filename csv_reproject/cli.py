import click


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
@click.argument('filename')
def cli(
        from_proj,
        from_x_column,
        from_y_column,
        from_x_format,
        from_y_format,
        to_proj,
        to_x_header,
        to_y_header,
        filename
):
    """Reproject a CSV from one Coordinate Reference System to another."""
    print(
        from_proj,
        from_x_column,
        from_y_column,
        from_x_format,
        from_y_format,
        to_proj,
        to_x_header,
        to_y_header,
        filename
    )


if __name__ == '__main__':
    cli()
