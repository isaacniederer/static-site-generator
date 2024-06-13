import os
import shutil

from htmlnode import (
    HTMLNode,
    ParentNode,
    LeafNode,
)

from block_markdown import(
    markdown_to_html_node,
)

def copy_static_to_public(s_path, p_path):
    if os.path.exists(p_path):
        shutil.rmtree(p_path)
    os.mkdir(p_path)
    for item in os.listdir(s_path):
        if os.path.isfile(s_path + item):
            shutil.copy(s_path + item, p_path + item)
            continue
        os.mkdir(p_path + item + "/")
        copy_static_to_public(s_path + item + "/", p_path + item + "/")

def extract_title(markdown):
    file = open(markdown)
    lines = file.read().split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    file.close()
    raise Exception("All pages need a single <h1> header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    sf = open(from_path)
    src_file = sf.read()
    tf = open(template_path)
    temp_file = tf.read()
    title = extract_title(from_path)
    content = markdown_to_html_node(src_file).to_html()
    temp_file = temp_file.replace("{{ Title }}", title)
    temp_file = temp_file.replace("{{ Content }}", content)
    if os.path.exists(os.path.dirname(dest_path)) == False:
        os.mkdir(os.path.dirname(dest_path))
    df = open(dest_path, "w")
    df.write(temp_file)
    sf.close()
    tf.close()
    df.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        if os.path.isfile(dir_path_content+file):
            generate_page(dir_path_content + file, template_path, dest_dir_path + file[:len(file)-2] + "html")
            continue
        generate_pages_recursive(dir_path_content+file+"/", template_path, dest_dir_path+file+"/")

def main():
    copy_static_to_public("./static/", "./public/")

    generate_pages_recursive("./content/", "./template.html", "./public/")

main()
