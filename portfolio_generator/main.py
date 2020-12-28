from pathlib import Path
from typing import Optional

import typer

from .settings import PortfolioGenSettings

app = typer.Typer()


def main(
    site_dir: Path,
    output_dir: Path,
    config: Path = Path("./portfolio.json"),
):
    """
    Flow of site generator:
    1. Validate CLI args and config file format
    2. Fetch/generate all resources asynchronously
    3. Once all resources are fetched successfully, run templating with Jinja2 on the site dir
    4. Output all built files to the output directory
    """
    pass


if __name__ == "__main__":
    typer.run(main)
