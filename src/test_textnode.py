import unittest

from textnode import TextNode
from main import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("\nTesting to see if __eq__() method works")
        node = TextNode("This is a text node", "bold", "http://boot.dev")
        node2 = TextNode("This is a text node", "bold", "http://boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        exp_string = "TextNode(This is a text node, bold, http://boot.dev)"
        text_node = TextNode("This is a text node", "bold", "http://boot.dev")
        new_string = str(text_node)
        print(f"\nExpected Representation: {exp_string}")
        print(f"Actual Representation: {new_string}")
        self.assertEqual(exp_string, new_string)

    def test_delimiter_split(self):
        text_type_text = "text"
        text_type_bold = "bold"
        text_type_italic = "italic"
        text_type_code = "code"
        text_type_link = "link"
        text_type_image = "image"
        print("\n========================================================")
        print("checking to see if the delimiter split is working correctly")
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(3, len(new_nodes))
        print("========================================================\n")

    def test_url_none(self):
        print("\nTesting equality in the case of url == None")
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
