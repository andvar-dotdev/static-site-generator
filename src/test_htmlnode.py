import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node: HTMLNode = HTMLNode("p", "This is a piece of text in a paragraph.")
        self.assertEqual(node.tag, "p")

    def test_value(self):
        node: HTMLNode = HTMLNode("p", "This is a piece of text in a paragraph.")
        self.assertEqual(node.value, "This is a piece of text in a paragraph.")

    def test_repr(self):
        node: HTMLNode = HTMLNode("p", "This is a piece of text in a paragraph.")
        self.assertEqual(repr(node), "HTMLNode(p, This is a piece of text in a paragraph., None, None)")


if __name__ == "__main__":
    unittest.main()
