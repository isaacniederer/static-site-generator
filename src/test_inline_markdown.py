import unittest

from inline_markdown import(
        split_nodes_delimiter,
        extract_markdown_images,
        extract_markdown_links,
        split_nodes_image,
        split_nodes_link,
        text_to_textnodes
    )

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image
    )

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_node = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("bolded", text_type_bold),
                    TextNode(" word", text_type_text), 
                ],
                new_node, 
            )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_node = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" word", text_type_text), 
                ],
                new_node, 
            )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_node = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
                [
                    TextNode("This is text with an ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(" word", text_type_text), 
                ],
                new_node, 
            )

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_split_nodes_image(self):
        node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",text_type_text,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("This is text with an ", text_type_text),
                    TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    TextNode(" and another ", text_type_text),
                    TextNode(
                        "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                    ),
                ],
                new_nodes
            )


    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text
            )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
                [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("link", text_type_link, "https://www.example.com"),
                    TextNode(" and ", text_type_text),
                    TextNode("another", text_type_link, "https://www.example.com/another")
                ],
                new_nodes
            )

    def test_text_to_textnodes(self):
        text_nodes = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)")
        self.assertEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            text_nodes
        )

    def test_text_to_textnodes2(self):
        text_nodes = text_to_textnodes("This is *text* with a `code block` and a [link](https://boot.dev)** that contains an **![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)")
        self.assertEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_italic),
                TextNode(" with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" that contains an ", text_type_bold),
                TextNode(
                    "image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
                ),
            ],
            text_nodes
        )



if __name__ == "__main__":
    unittest.main()
