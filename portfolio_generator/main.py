from pathlib import Path
from typing import Optional

import typer

from .settings import PortfolioGenSettings

app = typer.Typer()


def main(
    site_dir: Path,
    config: Path = Path("./portfolio.json"),
):
    pass


if __name__ == "__main__":
    typer.run(main)
