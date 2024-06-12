import unittest

from block_markdown import(
        markdown_to_blocks,
        block_to_block_type,
        markdown_to_html_node,
        block_type_paragraph,
        block_type_heading,
        block_type_code,
        block_type_quote,
        block_type_unordered_list,
        block_type_ordered_list,
    )

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks_length(self):
        text = "# This is a heading\n\n"
        text += "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
        text += "* This is a list item\n"
        text += "* This is another list item\n"
        self.assertEqual(len(markdown_to_blocks(text)), 3)

    def test_markdown_to_blocks_values(self):
        text = "# This is a heading\n\n"
        text += "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
        text += "* This is a list item\n"
        text += "* This is another list item"
        self.assertEqual(
                [
                    "# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is a list item * This is another list item"
                ],
                markdown_to_blocks(text)
            )

    def test_block_to_heading(self):
        text = "### This is a heading"
        self.assertEqual(block_type_heading, block_to_block_type(text))

    def test_block_to_code(self):
        text = """```
        This is a block of code
        ```"""
        self.assertEqual(block_type_code, block_to_block_type(text))
       
    def test_block_to_quote(self):
        text = """>YOU TURNED HER AGAINST ME!?
>You have done that yourself.
>YOU WILL NOT TAKE HER FROM ME!!!
>Your anger and your lust for power have already done that."""
        self.assertEqual(block_type_quote, block_to_block_type(text))

    def test_block_to_unordered_list(self):
        text = """* This is an item
* This is another item
- What do you know, a third item
* Howdy doody, a fourth"""
        self.assertEqual(block_type_unordered_list, block_to_block_type(text))

    def test_unordered_list_without_bullet(self):
        text = """* This is an item
 This is another item
- What do you know, a third item
* Howdy doody, a fourth"""
        self.assertNotEqual(block_type_unordered_list, block_to_block_type(text))
        self.assertEqual(block_type_paragraph, block_to_block_type(text))

    def test_block_to_ordered_list(self):
        new_text = """1. Go to Tempoross
2. Get 80 fishing and 40 something construction
3. Go to Wintertodt
4. Get 80 firemaking and in the 50s of construction
5. Train as much construction as possible with planks
6. Start grinding slayer along side combats"""
        self.assertEqual(block_type_ordered_list, block_to_block_type(new_text))

    def test_ordered_list_with_mistake(self):
        new_text = """1. Go to Tempoross
2. Get 80 fishing and 40 something construction
3. Go to Wintertodt
4. Get 80 firemaking and in the 50s of construction
5.Train as much construction as possible with planks
6. Start grinding slayer along side combats"""
        self.assertNotEqual(block_type_ordered_list, block_to_block_type(new_text))
        self.assertEqual(block_type_paragraph, block_to_block_type(new_text))

    def test_markdown_to_html_node(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""
        print(markdown_to_html_node(text))

    def test_markdown_to_html_node2(self):
        text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        print(markdown_to_html_node(text))

    def test_markdown_from_boot(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_markdown_html(self):
        md = """
# Star Wars

My favorite quote is

> YOU WILL NOT TAKE HER FROM ME!
> Your anger and lust for power has already done that

Thank you for your time

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual("<div><h1>Star Wars</h1><p>My favorite quote is</p><blockquote>YOU WILL NOT TAKE HER FROM ME! Your anger and lust for power has already done that</blockquote><p>Thank you for your time</p></div>", html)

    def test_lists(self):
        self.maxDiff = None
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()
