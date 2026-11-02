import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_notequal(self):
        node = TextNode("This is an image node", TextType.IMAGE)
        node2 = TextNode("This is a link node", TextType.LINK, "https://some-url.com")
        self.assertNotEqual(node, node2)

    def test_urlNone(self):
        node = TextNode("This is an image node", TextType.IMAGE, None)
        node2 = TextNode("This is an image node", TextType.IMAGE, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
