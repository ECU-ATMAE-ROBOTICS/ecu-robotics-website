from datetime import datetime
from typing import Dict, Any, List, TypedDict
import yaml
from pathlib import Path


class Project(TypedDict):
    name: str
    description: str
    image: str
    tags: List[str]


class PageConfig(TypedDict):
    template: str
    context: Dict[str, Any]


def load_config():
    config_dir = Path("config")

    try:
        with open(config_dir / "settings.yaml") as f:
            common_vars = yaml.safe_load(f) or {}
        common_vars["current_year"] = datetime.now().year

        with open(config_dir / "projects_list.yaml") as f:
            projects_data = yaml.safe_load(f) or []

        pages = {}
        for page_file in (config_dir / "pages").glob("*.yaml"):
            with open(page_file) as f:
                page_name = f"{page_file.stem}.html"
                pages[page_name] = yaml.safe_load(f) or {"template": "", "context": {}}

        if "projects.html" in pages:
            pages["projects.html"]["context"]["projects"] = projects_data

        return common_vars, projects_data, pages

    except FileNotFoundError as e:
        raise Exception(f"Missing config file: {e.filename}")
    except yaml.YAMLError as e:
        raise Exception(f"Invalid YAML: {str(e)}")


COMMON_VARS, PROJECTS_DATA, PAGES = load_config()
