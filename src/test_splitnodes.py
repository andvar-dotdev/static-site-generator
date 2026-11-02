import unittest
from splitters import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
    def test_emptynodes(self):
        old_nodes = []
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.TEXT)
        self.assertEqual(new_nodes, [])

    def test_singlenode(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_multiplenodes(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a **bold block** word", TextType.TEXT)
        node3 = TextNode("This is text with an _italic block_ word", TextType.TEXT)
        new_nodes1 = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        new_nodes2 = split_nodes_delimiter(new_nodes1, "**", TextType.BOLD)
        new_nodes3 = split_nodes_delimiter(new_nodes2, "_", TextType.ITALIC)

        self.assertEqual(new_nodes3, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])

    def test_twopairs(self):
        node = TextNode("This is text with a `code block` word and another `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word and another ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_delimeteratstart(self):
        node = TextNode("`code block` This is text with delimiter at the start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("code block", TextType.CODE),
            TextNode(" This is text with delimiter at the start", TextType.TEXT),
        ])

    def test_delimeteratend(self):
        node = TextNode("This is text with delimiter at the end `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with delimiter at the end ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ])

    def test_unclosed(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
