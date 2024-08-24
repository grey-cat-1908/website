import os
import shutil
import json
import mistune

markdown_renderer = mistune.create_markdown(
    plugins=[
        "math",
        "strikethrough",
        "footnotes",
        "table",
        "url",
        "task_lists",
        "abbr",
        "mark",
        "subscript",
        "spoiler",
    ]
)

shutil.rmtree("build", ignore_errors=True)
os.makedirs("build")

with open("template.html", "r") as template_file:
    template_text = template_file.read()

with open("blog_template.html", "r") as blog_template_file:
    blog_template_text = blog_template_file.read()

with open("meta.json", "r") as meta_file:
    base_meta = json.load(meta_file)


def parse_meta(meta_data):
    """Generate meta tags for the HTML head section."""
    meta_tags = []

    for key, value in meta_data.get("tags", {}).items():
        meta_tags.append(f'<meta name="{key}" content="{value}">')

    for key, value in meta_data.get("og", {}).items():
        meta_tags.append(f'<meta property="og:{key}" content="{value}">')

    return "".join(meta_tags)


def generate_html_content(directory, filename, is_blog=False):
    """Generate HTML content from a markdown file and metadata."""
    file_path = os.path.join(directory, filename)

    with open(file_path, "r") as file:
        md_text = file.read()

    meta_path = os.path.join(directory, "meta.json")
    meta = base_meta
    if os.path.exists(meta_path):
        with open(meta_path, "r") as meta_file:
            meta = json.load(meta_file)

    meta_data = parse_meta(meta)

    template_to_use = blog_template_text if is_blog else template_text

    return (
        template_to_use.replace("{{%CONTENT%}}", markdown_renderer(md_text))
        .replace("{{%TITLE%}}", meta.get("title", ""))
        .replace("{{%META%}}", meta_data)
    )


def copy_static_files(static_dir, build_dir="build"):
    """Copy static files and directories to the build folder."""
    for element in os.listdir(static_dir):
        src = os.path.join(static_dir, element)
        dst = os.path.join(build_dir, element)

        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy(src, dst)


def process_content_directory(source_dir, target_dir):
    """Recursively process the content directory and generate HTML files."""
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename)

        if os.path.isdir(source_path):
            os.makedirs(target_path, exist_ok=True)
            process_content_directory(source_path, target_path)
        else:
            if filename.endswith(".md"):
                is_blog = "blog" in os.path.relpath(source_path, start="content").split(
                    os.sep
                )

                html_filename = os.path.splitext(filename)[0] + ".html"
                output_file = os.path.join(target_dir, html_filename)
                content = generate_html_content(source_dir, filename, is_blog=is_blog)

                with open(output_file, "w") as file:
                    file.write(content)


copy_static_files("static")
process_content_directory("content", "build")
