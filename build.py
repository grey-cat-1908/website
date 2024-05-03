import os
import shutil
import json

import mistune

render = mistune.create_markdown(
    plugins=['math', 'strikethrough', 'footnotes', 'table', 'url', 'task_lists', 'abbr', 'mark', 'subscript', 'spoiler']
)

try:
    shutil.rmtree("build")
except:
    pass

os.mkdir("build")

template_file = open('template.html', "r")
template_text = template_file.read()
template_file.close()

base_meta_file = open('meta.json', "r")
base_meta = json.loads(base_meta_file.read())
base_meta_file.close()

def parse_meta(data):
    result = ""

    for key, value in data['tags'].items():
        result += f'<meta name="{key}" content="{value}">\n'
    
    for key, value in data['og'].items():
        result += f'<meta property="og:{key}" content="{value}">\n'

    return result

def gen_file(directory, filename):
    file = open(directory + filename, "r")
    md_text = file.read()
    file.close()

    try:
        file = open(directory + 'meta.json', "r")
        meta = json.loads(file.read())
        file.close()
    except:
        meta = base_meta
    
    meta_data = parse_meta(meta)

    return template_text.replace("{{%CONTENT%}}", render(md_text)).replace("{{%TITLE%}}", meta['title']).replace("{{%META%}}", meta_data)

def go_through(directory):
    for filename in os.listdir(directory):
        _, _, fier = directory.partition('/')
        if len(fier) != 0: fier += "/"

        if len(filename.split(".")) == 1:
            os.makedirs(f'build/{fier}{filename}')
            go_through(directory + "/" + filename)
        else:
            if filename.split(".")[1] == "json":
                continue
            for ofn in os.listdir("static"):
                try:
                    if len(ofn.split(".")) == 1:
                        shutil.copytree(f"{os.getcwd()}/static/{ofn}", f"{os.getcwd()}/build/{fier}{ofn}")
                    else:
                        shutil.copy(f"{os.getcwd()}/static/{ofn}", f"{os.getcwd()}/build/{fier}{ofn}")
                except:
                    pass

            content = gen_file(f"{os.getcwd()}/{directory}/", filename)
            loc = fier + filename.split(".")[0] + '.html'

            file = open(f"{os.getcwd()}/build/{loc}", "a")    
            file.write(content)
            file.close()

go_through("content")
