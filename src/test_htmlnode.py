import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

        Rhys_node = LeafNode('blabla', "son")
        Gage_node = LeafNode('biggie', 'also son')
        Lori_node = ParentNode('dev', [Rhys_node,Gage_node])
        self.assertEqual(Lori_node.to_html(), '<dev><blabla>son</blabla><biggie>also son</biggie></dev>')
        

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

        chip_node= LeafNode('plas', 'brain')
        cord_node = LeafNode('c', 'rubber', {'color': 'black', 'size':'long', 'wattage':" 40 volts"})
        converter_node = LeafNode('e','electrical converter')
        ram_node = LeafNode('s', '32 gb')
        power_node = ParentNode('p', [cord_node, converter_node])
        Computer_node = ParentNode('c', [chip_node, power_node, ram_node])
        self.assertEqual(Computer_node.to_html(), '<c><plas>brain</plas><p><c color="black" size="long" wattage=" 40 volts">rubber</c><e>electrical converter</e></p><s>32 gb</s></c>')
        