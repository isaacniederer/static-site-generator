from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

ACCEPTED_TYPES = [
        "text_type_text",
        "text_type_bold",
        "text_type_italic",
        "text_type_code",
        "text_type_link",
        "text_type_image"
        ]


def main():
    new_node = TextNode("This is an image node", "image", "https://www.boot.dev")
    new_leaf = text_node_to_html_node(new_node)
    print(new_leaf)

def text_node_to_html_node(text_node):
    print(f"\n\n text_type_{text_node.text_type} \n\n")
    if f"text_type_{text_node.text_type}" in ACCEPTED_TYPES:
        if f"text_type_{text_node.text_type}" == ACCEPTED_TYPES[0]:
            return LeafNode(None, text_node.text)
        elif f"text_type_{text_node.text_type}" == ACCEPTED_TYPES[1]:
            return LeafNode("b", text_node.text)
        elif f"text_type_{text_node.text_type}" == ACCEPTED_TYPES[2]:
            return LeafNode("i", text_node.text)
        elif f"text_type_{text_node.text_type}" == ACCEPTED_TYPES[3]:
            return LeafNode("code", text_node.text)
        elif f"text_type_{text_node.text_type}" == ACCEPTED_TYPES[4]:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        elif f"text_type_{text_node.text_type}" == ACCEPTED_TYPES[5]:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    else:
        raise Exception("What the fuck is even happening")

main()
