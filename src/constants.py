from pathlib import Path


class Paths:
    """Centralized location for all file paths."""

    ROOT = Path(__file__).parent.parent
    OUTPUT = ROOT / "docs"
    STATIC = ROOT / "static"
    TEMPLATES = ROOT / "templates"
    SCSS_INPUT = STATIC / "css" / "stylesheet.scss"
    CSS_OUTPUT = OUTPUT / "static" / "css" / "stylesheet.css"

    @classmethod
    def ensure_directories_exist(cls):
        """Create all required directories if they don't exist."""
        required_dirs = [
            cls.OUTPUT / "static/css",
            cls.OUTPUT / "static/img",
            cls.CSS_OUTPUT.parent,
        ]
        for directory in required_dirs:
            directory.mkdir(parents=True, exist_ok=True)
