import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from textdelimiter import split_nodes_delimiter


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

    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

        Kelleynode = TextNode('Listen _fellas_, we got to be _better_', TextType.TEXT)
        Zaknode = TextNode('Listen, _I am the best_, and _never_ forget it', TextType.TEXT)
        ZK_new_nodes = split_nodes_delimiter([Kelleynode,Zaknode], '_', TextType.ITALIC)
        self.assertEqual(ZK_new_nodes, [
            TextNode('Listen ', TextType.TEXT),
            TextNode('fellas', TextType.ITALIC),
            TextNode(', we got to be ', TextType.TEXT),
            TextNode('better', TextType.ITALIC),
            TextNode('', TextType.TEXT),
            TextNode('Listen, ', TextType.TEXT),
            TextNode('I am the best', TextType.ITALIC),
            TextNode(', and ', TextType.TEXT),
            TextNode('never', TextType.ITALIC),
            TextNode(' forget it', TextType.TEXT)
        ])
        
        

if __name__ == "__main__":
    unittest.main()
