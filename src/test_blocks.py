import unittest

from blocks import BlockType, block_to_block_type

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