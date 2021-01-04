from pathlib import Path

import pydantic
import typer
from click.exceptions import Exit

from .builder import build_site
from .resource_fetchers.google_doc import GoogleDocExportFetcher
from .settings import PortfolioGenSettings

app = typer.Typer()


def main(
    site_dir: Path = typer.Argument(..., exists=True, file_okay=False),
    output_dir: Path = typer.Argument(..., exists=True, file_okay=False),
    config: Path = typer.Argument(Path("portfolio.toml"), exists=True, dir_okay=False),
):
    """
    Flow of site generator:
    1. Validate CLI args and config file format
    2. Fetch/generate all resources asynchronously
    3. Once all resources are fetched successfully, run templating with Jinja2 on the site dir
    4. Output all built files to the output directory
    """
    try:
        portfolio = PortfolioGenSettings.from_toml(config.absolute())
    except pydantic.ValidationError as e:
        print(f"Error validating config file: {e}")
        raise Exit(1) from e

    print(f"Loaded portfolio: {portfolio}")

    # fetch resources asynchronously
    fetcher = GoogleDocExportFetcher(settings=PortfolioGenSettings)
    fetcher.fetch()

    build_site(portfolio, {}, site_dir, output_dir)


def run_cli():
    typer.run(main)
