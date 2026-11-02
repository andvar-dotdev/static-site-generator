import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_numerous_grandchildren(self):
        grandchild_node1 = LeafNode("b", "Bold text")
        grandchild_node2 = LeafNode(None, "Normal text")
        grandchild_node3 = LeafNode("i", "Italic text")
        grandchild_node4 = LeafNode(None, "Normal text")
        child_node1 = ParentNode("p",
            [
                grandchild_node1,
                grandchild_node2,
                grandchild_node3,
                grandchild_node4
            ]
        )
        child_node2 = ParentNode("span", [])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p><span></span></div>",
        )

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

if __name__ == "__main__":
    unittest.main()
