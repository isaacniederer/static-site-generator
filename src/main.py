import re

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

ACCEPTED_TYPES = [
        "text_type_text",
        "text_type_bold",
        "text_type_italic",
        "text_type_code",
        "text_type_link",
        "text_type_image",
        ]

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
    if f"text_type_{text_node.text_type}" in ACCEPTED_TYPES:
        if f"text_type_{text_node.text_type}" == "text_type_text":
            return LeafNode(None, text_node.text)
        elif f"text_type_{text_node.text_type}" == "text_type_bold":
            return LeafNode("b", text_node.text)
        elif f"text_type_{text_node.text_type}" == "text_type_italic":
            return LeafNode("i", text_node.text)
        elif f"text_type_{text_node.text_type}" == "text_type_code":
            return LeafNode("code", text_node.text)
        elif f"text_type_{text_node.text_type}" == "text_type_link":
            return LeafNode("a", text_node.text, {"href":text_node.url})
        elif f"text_type_{text_node.text_type}" == "text_type_image":
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    else:
        raise Exception("What the fuck is even happening")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_list = []
    for item in old_nodes:
        if item.text_type != text_type_text:
            return_list.append(item)
        else:
            if delimiter in item.text:
                new_list = item.text.split(delimiter)
                if len(new_list) != 3:
                    raise Exception("Incorrect Markdown syntax")
                return_list.extend([
                    TextNode(new_list[0], text_type_text),
                    TextNode(new_list[1], text_type),
                    TextNode(new_list[2], text_type_text)
                    ]
                    )

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def main():
    #new_node = TextNode("This is an image node", "image", "https://www.boot.dev")
    #new_leaf = text_node_to_html_node(new_node)
    #print(new_leaf)
    print( split_nodes_delimiter(
        [TextNode("This is text with a `code block` word", text_type_text), TextNode("This is a **bold** word", text_type_text)],
        "`", text_type_code)
        )
    print("\n\n")
    print(extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"))
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text))

main()
