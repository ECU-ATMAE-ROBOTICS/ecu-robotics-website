from jinja2 import Environment, FileSystemLoader
import sass
import shutil
from pathlib import Path
from typing import Dict, Any
from .constants import Paths

def compile_scss() -> None:
    """Compile SCSS to CSS with error handling."""
    try:
        compiled_css = sass.compile(
            filename=str(Paths.SCSS_INPUT),
            output_style="expanded"
        )
        Paths.CSS_OUTPUT.write_text(compiled_css)
    except (sass.CompileError, IOError) as e:
        raise RuntimeError(f"SCSS compilation failed: {e}")

def copy_static_files() -> None:
    """Copy static files to output directory, excluding SCSS files."""
    for item in Paths.STATIC.rglob("*"):
        if item.is_file() and item.suffix != ".scss":
            relative_path = item.relative_to(Paths.STATIC)
            dest_path = Paths.OUTPUT / "static" / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(item, dest_path)

def setup_jinja() -> Environment:
    """Configure and return Jinja2 environment."""
    return Environment(loader=FileSystemLoader(Paths.TEMPLATES))