import click
from pyproj import Proj, transform


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

    # Todo: Create CsvProjReader class with:
    # - __init(
    #   input_filename: str,
    #   from_x_column: str,
    #   from_y_column: str,
    #   from_x_format: str,
    #   from_y_format: str
    # )
    #   - Throw exception if x and y columns do not exist in the CSV's header.
    #   -
    # - read_headers() -> List[str]
    # - read_proj_rows() -> List[CsvProjRow] (Generator)

    # Todo: Create CsvProjRow class with:
    # - get_values() -> List[str]
    # - get_x_value() -> float
    # - get_y_value() -> float

    # Todo: Create Reprojector class with:
    # Todo: Perhaps this already exists as pyproj.Transformer?
    # - init(
    #   from_proj: Proj
    #   to_proj: Proj
    # )
    # - transform(x: float, y: float) -> Tuple[x: float, y: float]

    # Todo: Create CsvProjWriter class with:
    # - __init(
    #   output_filename: str,
    #   to_x_header: str,
    #   to_y_header: str
    # )
    # - write_headers(header: List[str])
    # - write_row(row: List[str], x: float, y: float)

    print(
        from_proj,
        from_x_column,
        from_y_column,
        from_x_format,
        from_y_format,
        to_proj,
        to_x_header,
        to_y_header,
        input_filename,
        output_filename
    )

    exit()

    reader = CsvProjReader(
        input_filename,
        from_x_column,
        from_y_column,
        from_x_format,
        from_y_format
    )

    writer = CsvProjWriter(
        output_filename,
        to_x_header,
        to_y_header
    )

    input_headers = reader.read_headers()
    writer.write_headers(input_headers)

    for csv_proj_row in reader.read_proj_rows():
        new_x, new_y = transform(
            from_proj,
            to_proj,
            csv_proj_row.get_x_value(),
            csv_proj_row.get_y_value()
        )
        writer.write_row(csv_proj_row.get_values(), new_x, new_y)




if __name__ == '__main__':
    cli()
