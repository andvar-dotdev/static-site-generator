import unittest
from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Follow this link!", {"href": "https://some-random-domain.com"})
        self.assertEqual(node.to_html(), '<a href="https://some-random-domain.com">Follow this link!</a>')

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "This is code beep boop")
        self.assertEqual(node.to_html(), '<code>This is code beep boop</code>')

if __name__ == "__main__":
    unittest.main()
