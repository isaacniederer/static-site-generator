import re

from htmlnode import(
    HTMLNode,
    ParentNode,
    LeafNode,
)

from inline_markdown import(
    text_to_textnodes,
)

from textnode import(
    text_node_to_html_node,
)

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    new_block = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        mod_block = []
        lines = block.split("\n")
        for line in lines:
            if line == "":
                continue
            mod_block.append(line.strip())
        new_block.append(" ".join(mod_block))
    return new_block

def block_to_block_type(block):
    block_lines = block.split("\n")
    if "# " in block_lines[0]:
        return block_type_heading
    if "```" in block_lines[0] and "```" in block_lines[len(block_lines)-1]:
        return block_type_code
    for i in range(0, len(block_lines)):
        if block_lines[i] == "":
            continue
        if block_lines[i][0] != ">":
            break
        if i == len(block_lines)-1:
            return block_type_quote
    for i in range(0, len(block_lines)):
        if block_lines[i] == "":
            continue
        if block_lines[i][0] != "*" and block_lines[i][0] != "-":
            break
        if i == len(block_lines)-1:
            return block_type_unordered_list
    for i in range(0, len(block_lines)):
        str1 = block_lines[i][:3]
        str2 = f"{i+1}. "
        if str1 != str2:
            break
        if i == len(block_lines)-1:
            return block_type_ordered_list
    return block_type_paragraph

def block_to_html_paragraph(text):
    children = []
    children_text_nodes = text_to_textnodes(text)
    for node in children_text_nodes:
        children.append(text_node_to_html_node(node))
    return ParentNode("p", children)

def block_to_html_heading(text):
    i = text.count('#')
    children = []
    children_text_nodes = text_to_textnodes(text.replace("#", "").strip())
    for node in children_text_nodes:
        children.append(text_node_to_html_node(node))
    return ParentNode(f"h{i}", children)

def block_to_html_code(text):
    node = LeafNode("code", text)
    return ParentNode("pre", [node])

def block_to_html_quote(text):
    children = []
    children_text_nodes = text_to_textnodes(text.replace("> ", "").strip())
    for node in children_text_nodes:
        children.append(text_node_to_html_node(node))
    return ParentNode("blockquote", children)

def block_to_html_unordered_list(text):
    children = []
    lines = text.split("-")
    for line in lines:
        line_children = []
        if line == "":
            continue
        children_text_nodes = text_to_textnodes(line.strip())
        for node in children_text_nodes:
            line_children.append(text_node_to_html_node(node))
        children.append(ParentNode("li", line_children))
    return ParentNode("ul", children) 

def block_to_html_ordered_list(text):
    children = []
    new_lines = re.findall(r"[^\d\.]+",text)    
    for i in range(0, len(new_lines)):
        if new_lines[i] == "":
            continue
        line_children = []
        children_text_nodes = text_to_textnodes(new_lines[i].strip())
        for node in children_text_nodes:
            line_children.append(text_node_to_html_node(node))
        children.append(ParentNode("li", line_children))
    return ParentNode("ol", children) 

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_paragraph:
            children.append(block_to_html_paragraph(block))
        elif block_to_block_type(block) == block_type_heading:
            children.append(block_to_html_heading(block))
        elif block_to_block_type(block) == block_type_code:
            children.append(block_to_html_code(block))
        elif block_to_block_type(block) == block_type_quote:
            children.append(block_to_html_quote(block))
        elif block_to_block_type(block) == block_type_unordered_list:
            children.append(block_to_html_unordered_list(block))
        elif block_to_block_type(block) == block_type_ordered_list:
            children.append(block_to_html_ordered_list(block))
    return ParentNode("div", children)

