from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import shutil
import sass

output_dir = Path("docs")
static_dir = Path("static")
templates_dir = Path("templates")
scss_input = static_dir / "css" / "stylesheet.scss"
css_output = output_dir / "static" / "css" / "stylesheet.css"

(output_dir / "static/css").mkdir(parents=True, exist_ok=True)
(output_dir / "static/img").mkdir(parents=True, exist_ok=True)


def compile_scss():
    compiled_css = sass.compile(filename=str(scss_input), output_style="expanded")
    css_output.parent.mkdir(parents=True, exist_ok=True)
    css_output.write_text(compiled_css)


compile_scss()

env = Environment(loader=FileSystemLoader(templates_dir))

common_vars = {
    "static_path": "static",
    "css_path": "static/css/stylesheet.css",
    "logo_path": "static/img/ecu_pirate_robot_logo.png",
    "home_link": "index.html",
    "projects_link": "projects.html",
    "contact_link": "contact.html",
    "current_year": 2025,
}

projects_data = [
    {
        "name": "ATMAE Robotics Competition",
        "description": "Latin Placeholder Text (lol)",
        "image": "jamie_working.jpg",
        "tags": ["Autonomous", "Computer Vision", "Competition"],
    }
]

pages = {
    "index.html": (
        "home.html",
        {
            "title": "ECU ATMAE Robotics - Home",
            "description": "Official website for ECU ATMAE Robotics Team - Innovating the future of automation and robotics technology",
            "active_page": "home",
        },
    ),
    "projects.html": (
        "projects.html",
        {
            "title": "ECU ATMAE Robotics - Projects",
            "description": "ECU ATMAE Robotics Projects - Our robotics projects and achievements",
            "active_page": "projects",
            "projects": projects_data,
        },
    ),
    "contact.html": (
        "contact.html",
        {
            "title": "ECU ATMAE Robotics - Contact",
            "description": "Contact ECU ATMAE Robotics Team - Get in touch with our team members and leadership",
            "active_page": "contact",
            "faculty_advisor": {"name": "Dr. John Smith", "email": "smithj@ecu.edu"},
            "meeting_times": {
                "days": "Tuesdays & Thursdays",
                "time": "5:00 PM - 7:00 PM",
                "location": "Engineering Building Room 205",
            },
        },
    ),
}

for filename, (template_name, context) in pages.items():
    template = env.get_template(template_name)
    html = template.render(**common_vars, **context)
    (output_dir / filename).write_text(html)


def copy_static_files():
    for item in static_dir.rglob("*"):
        if item.is_file():
            relative_path = item.relative_to(static_dir)

            if relative_path.suffix == ".scss" or "css" in relative_path.parts:
                continue

            dest_path = output_dir / "static" / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(item, dest_path)


copy_static_files()

print(
    f"""
✅ Website generated successfully in the '{output_dir}' directory!
Pages created:
- index.html (Home)
- projects.html (Projects)
- contact.html (Contact)

Static files copied to '{output_dir}/static/' and SCSS compiled to CSS.
"""
)
