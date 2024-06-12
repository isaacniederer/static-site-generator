import unittest

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image
    )

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

    def test_url_none(self):
        print("\nTesting equality in the case of url == None")
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
