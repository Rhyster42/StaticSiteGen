import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        nodeRhys = TextNode("Hey it's you", TextType.LINK)
        nodeGage = TextNode("Hey it's still you", TextType.LINK)
        self.assertNotEqual(nodeRhys, nodeGage)

        nodeKellan = TextNode("Bro", TextType.BOLD)
        nodeOli = TextNode("Bro", TextType.BOLD)
        self.assertEqual(nodeKellan, nodeOli)

        nodeSarah = TextNode("Hey Girl",TextType.ITALIC, "www.imright.com")
        nodeNatalie = TextNode("Hey Girl", TextType.ITALIC)
        self.assertNotEqual(nodeSarah, nodeNatalie)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        bold_node = TextNode('This is a bold text node', TextType.BOLD)
        bold_html = text_node_to_html_node(bold_node)
        self.assertEqual(bold_html.tag, 'b')
        self.assertEqual(bold_html.value, 'This is a bold text node')

        link_node = TextNode('alt text for image', TextType.IMAGE, 'www.imageurl.com')
        link_html = text_node_to_html_node(link_node)
        self.assertEqual(link_html.tag, 'img')
        self.assertEqual(link_html.value, None)
        self.assertEqual(link_html.props, {'src':'www.imageurl.com', 'alt': 'alt text for image'})
        

if __name__ == "__main__":
    unittest.main()
