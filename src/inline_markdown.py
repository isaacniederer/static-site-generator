import re

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image
    )

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_list = []
    for item in old_nodes:
        if item.text_type != text_type_text:
            return_list.append(item)
            continue
        split_list = []
        new_list = item.text.split(delimiter)
        if len(new_list) == 0:
            raise Exception("Incorrect Markdown syntax")
        for i in range(0, len(new_list)):
            if new_list[i] == "":
                continue
            if i%2 == 0:
                split_list.append(TextNode(new_list[i], text_type_text))
            else:
                split_list.append(TextNode(new_list[i], text_type))
        return_list.extend(split_list)
    return return_list
                    
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    return_list = []
    for item in old_nodes:
        new_list = []
        new_nodes = extract_markdown_images(item.text)
        if len(new_nodes) == 0:
            return_list.append(item)
            continue
        string = item.text.split(f"![{new_nodes[0][0]}]({new_nodes[0][1]})",2) 
        for i in range(0, len(new_nodes)):
            new_string = string[1]
            if string[0] != "":
                new_list.append(TextNode(string[0], text_type_text))
            new_list.append(TextNode(new_nodes[i][0], text_type_image, new_nodes[i][1]))
            if i == len(new_nodes)-1:
                if string[1] != "":
                    new_list.append(TextNode(string[1], text_type_text))
                continue
            string = new_string.split(f"![{new_nodes[i+1][0]}]({new_nodes[i+1][1]})", 2)


        return_list.extend(new_list)
    return return_list

def split_nodes_link(old_nodes):
    return_list = []
    for item in old_nodes:
        new_list = []
        new_nodes = extract_markdown_links(item.text)
        if len(new_nodes) == 0:
            return_list.append(item)
            continue
        string = item.text.split(f"[{new_nodes[0][0]}]({new_nodes[0][1]})",2)
        if len(string) < 2:
            raise Exception("Links not found in the string")
        for i in range(0, len(new_nodes)):
            new_string = string[1]
            if string[0] != "":
                new_list.append(TextNode(string[0], text_type_text))
            new_list.append(TextNode(new_nodes[i][0], text_type_link, new_nodes[i][1]))
            if i == len(new_nodes)-1:
                if string[1] != "":
                    new_list.append(TextNode(string[1], text_type_text))
                continue
            string = new_string.split(f"[{new_nodes[i+1][0]}]({new_nodes[i+1][1]})", 2)


        return_list.extend(new_list)
    return return_list

def text_to_textnodes(text):
    new_nodes = split_nodes_delimiter([TextNode(text, text_type_text)], "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

