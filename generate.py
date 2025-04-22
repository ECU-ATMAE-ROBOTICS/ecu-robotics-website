import sys
from src.constants import Paths
from src.config import COMMON_VARS, PROJECTS_DATA, PAGES
from src.utils import compile_scss, copy_static_files, setup_jinja


def generate_pages(env):
    """Generate all HTML pages from templates."""
    for output_file, page_config in PAGES.items():
        template = env.get_template(page_config["template"])

        final_output_file = "index.html" if output_file == "home.html" else output_file

        context = {
            **COMMON_VARS,
            **page_config.get("context", {}),
            "current_page": output_file,
        }

        if output_file == "projects.html":
            context["projects"] = PROJECTS_DATA

        html = template.render(**context)
        output_path = Paths.OUTPUT / final_output_file
        output_path.write_text(html)
        print(f"• Generated: {final_output_file}")


def main():
    try:
        print("🚀 Starting website generation...")
        print(f"• Found {len(PROJECTS_DATA)} projects")
        print(f"• Generating {len(PAGES)} pages")

        Paths.ensure_directories_exist()

        compile_scss()
        copy_static_files()

        env = setup_jinja()
        generate_pages(env)

        print(
            f"""
✅ Success! Website generated in '{Paths.OUTPUT}'
📄 Pages: {', '.join(['index.html' if x == 'home.html' else x for x in PAGES.keys()])}
🖼️  Projects: {len(PROJECTS_DATA)} loaded
"""
        )
    except Exception as e:
        print(f"❌ Generation failed: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
