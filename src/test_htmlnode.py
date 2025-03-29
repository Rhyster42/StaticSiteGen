import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        nodeRhys = HTMLNode("p", "Homeless Hermit", None , {"roommate":"Kellan", "best friend":"Mitchell","Mother":"Lori"})
        print(nodeRhys.props_to_html())
        
        kiddies = []
        nodeAna = HTMLNode("a", "Ferocious Mother", kiddies, {"Husband":"Louis", "Daughter": "Evichka", "Son":"River"} )
        print(nodeAna.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')

        nodeRhys = LeafNode('a', "Good Job Buddy", {'website':'www.imright.com'})
        self.assertEqual(nodeRhys.to_html(), '<a website="www.imright.com">Good Job Buddy</a>')

        nodeleafheader = LeafNode('h3', "This is my header!!!")
        self.assertEqual(nodeleafheader.to_html(), '<h3>This is my header!!!</h3>')