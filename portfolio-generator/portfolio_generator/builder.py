from pathlib import Path
from typing import Dict

from jinja2 import Environment, FileSystemLoader

from .settings import PortfolioGenSettings


def build_site(
    portfolio: PortfolioGenSettings, resources: Dict, src_dir: Path, out_dir: Path
):
    env = Environment(
        loader=FileSystemLoader(str(src_dir.absolute())),
        autoescape=True,
    )

    print(f"Available templates in {src_dir}: {env.list_templates()}")

    for template_name in env.list_templates():
        # TODO: Make this more robust, don't only support html and support more than just one template
        # named base.html
        if not template_name.endswith("html") or template_name.startswith("base"):
            print("Skipping template: {template_name}...")
            continue

        print(f"Filling template: {template_name}")
        template = env.get_template(template_name)
        rendered_template = template.render(portfolio=portfolio, resources=resources)
        _write_rendered_template_to_file(rendered_template, out_dir, template_name)

    # assert that resources were used
    print("Done filling templates")


def _write_rendered_template_to_file(
    rendered_template: str, out_dir: Path, relative_path: str
):
    output_path = Path.joinpath(out_dir, relative_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered_template)
