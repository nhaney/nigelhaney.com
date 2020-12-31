from pathlib import Path
from typing import Dict

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .settings import PortfolioGenSettings


def build_site(
    portfolio: PortfolioGenSettings, resources: Dict, src_dir: Path, out_dir: Path
):
    env = Environment(
        loader=FileSystemLoader(str(src_dir.absolute())),
        autoescape=True,
    )

    print(f"Available templates: {env.list_templates()}")
