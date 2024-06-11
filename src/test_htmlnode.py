import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!",{"href": "https://www.google.com"})
        print(node1.to_html())
        print(node2.to_html())

    def test_parent(self):
        print("\n==============================================================")
        print("Testing parent node for expected output")
        exp_str = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print("Expected output: " + exp_str)
        new_str = node.to_html()
        print("Actual output: " + new_str)
        if new_str == exp_str:
            print("PASSED")
            print("==============================================================\n")
            return
        print("FAILED")
        print("==============================================================\n")





if __name__ == "__main__":
    unittest.main()
