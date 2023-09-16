import os
import shutil

import mistune

render = mistune.create_markdown(
    plugins=['math', 'strikethrough', 'footnotes', 'table', 'url', 'task_lists', 'abbr', 'mark', 'subscript', 'spoiler']
    )

try:
    shutil.rmtree("build")
except:
    pass

os.mkdir("build")


for filename in os.listdir("static"):
    if len(filename.split(".")) == 1:
        shutil.copytree(f"{os.getcwd()}/static/{filename}", f"{os.getcwd()}/build/{filename}")
    else:
        shutil.copy(f"{os.getcwd()}/static/{filename}", f"{os.getcwd()}/build/{filename}")


template_file = open('template.html', "r")
template_text = template_file.read()
template_file.close()


def gen_file(directory):
    file = open(directory, "r")
    md_text = file.read()
    file.close()

    return template_text.replace("{{%CONTENT%}}", render(md_text))


for filename in os.listdir("content"):
    if len(filename.split(".")) == 1:
        content = gen_file(f"{os.getcwd()}/content/{filename}/index.md")
        loc = f"{filename}/index.html"
        os.makedirs(f'build/{filename}')
    else:
        content = gen_file(f"{os.getcwd()}/content/{filename}")
        loc = filename.split(".")[0] + '.html'

    file = open(f"{os.getcwd()}/build/{loc}", "a")
    file.write(content)
    file.close()