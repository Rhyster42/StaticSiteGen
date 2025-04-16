import unittest

from blocks import BlockType, block_to_block_type, markdown_to_html_node

class Blocks(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "#### This is a header."
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block2 = "```This should return a code." \
        "second line```"
        self.assertEqual(block_to_block_type(block2), BlockType.CODE)

        block3 = "> To be or not to be." \
        ">That is the question."
        self.assertEqual(block_to_block_type(block3), BlockType.QUOTE)

        block4 = "- this is a shitty list." \
        "- I forgot to order it." \
        "- So it should returns as an unordered list."
        self.assertEqual(block_to_block_type(block4), BlockType.UNORDERED_LIST)

        block5 = '1. This list is better.' \
        '2. I actually organized it.' \
        '3. Because I am awesome.'
        self.assertEqual(block_to_block_type(block5), BlockType.ORDERED_LIST)

    def test_paragraphs(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

    def test_codeblock(self):
        md = """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )