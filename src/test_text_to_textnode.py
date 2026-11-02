import unittest
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnode

class TestTexttoNode(unittest.TestCase):
    def test_emptytext(self):
        with self.assertRaises(Exception):
            text_to_textnode("")

    def test_Nonetext(self):
        with self.assertRaises(Exception):
            text_to_textnode(None)

    def test_text_to_node(self):
        text: str = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes: list[TextNode] = text_to_textnode(text)
        self.assertEqual(nodes, [
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
        ])

if __name__ == "__main__":
    unittest.main()
