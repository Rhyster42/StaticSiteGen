import unittest

from extractors import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_text_nodes, extract_title
from textnode import TextNode, TextType
from blocks import markdown_to_blocks


class TextExtractors(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        matches2 =extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches2)

        matches3 = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches3)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
            )
        
        node_link = TextNode("This is a text with a [link](https://i.imgur.com/kknjw.png) and second [second image](https://i.imgur.com/4thusle.png)", TextType.TEXT)
        new_link_nodes = split_nodes_link([node_link])
        self.assertListEqual([
            TextNode('This is a text with a ', TextType.TEXT),
            TextNode('link', TextType.LINK, 'https://i.imgur.com/kknjw.png'),
            TextNode(' and second ', TextType.TEXT),
            TextNode('second image', TextType.LINK, 'https://i.imgur.com/4thusle.png')
        ], new_link_nodes)

    def test_text_to_textnode(self):
        test_string = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        string_nodes = text_to_text_nodes(test_string)

        self.assertEqual([
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ], string_nodes)

        test_string_2 = '**Colt 45, and two zigzags**, baby thats all we _need._ We can go to the ![floor image](https://i.floors.com/fhduh.jpeg), out the door. Smoke that `tumbleweed`. Let the marijuana **burn** we can take our _turn_. Singin them dirty rap [rap link](www.songsandrapstuff.com). Stop!'
        string_nodes_2 = text_to_text_nodes(test_string_2)

        self.assertEqual([
            TextNode('Colt 45, and two zigzags', TextType.BOLD),
            TextNode(', baby thats all we ', TextType.TEXT),
            TextNode('need.', TextType.ITALIC),
            TextNode(' We can go to the ', TextType.TEXT),
            TextNode('floor image', TextType.IMAGE, 'https://i.floors.com/fhduh.jpeg'),
            TextNode(', out the door. Smoke that ', TextType.TEXT),
            TextNode('tumbleweed', TextType.CODE),
            TextNode('. Let the marijuana ', TextType.TEXT),
            TextNode('burn', TextType.BOLD),
            TextNode(' we can take our ', TextType.TEXT),
            TextNode('turn', TextType.ITALIC),
            TextNode('. Singin them dirty rap ', TextType.TEXT),
            TextNode('rap link', TextType.LINK, 'www.songsandrapstuff.com'),
            TextNode('. Stop!', TextType.TEXT)
            ], string_nodes_2)

    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
            ],
        )

        md2 = ("""
        First paragraph.

        Second paragraph.
        """)
        self.assertEqual(markdown_to_blocks(md2), [
        "First paragraph.",
        "Second paragraph."
        ])

        md3 = """
        First line.
        Second line.

        Next block.
        """
        self.assertEqual(markdown_to_blocks(md3), ["First line.\nSecond line.",
        "Next block."])

    def test_extract_title(self):
        md = """

        # This is the header

        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """

        self.assertEqual(extract_title(md), 'This is the header')

        md2 = """

        ## This is a decoy

        # This is the header

        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """

        self.assertEqual(extract_title(md2), 'This is the header')




if __name__ == "__main__":
    unittest.main()