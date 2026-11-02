import unittest
from splitters import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
    def test_emptynodes(self):
        old_nodes = []
        new_nodes1 = split_nodes_image(old_nodes)
        new_nodes2 = split_nodes_link(old_nodes)
        self.assertEqual(new_nodes1, [])
        self.assertEqual(new_nodes2, [])

    def test_singleimage(self):
        node = TextNode("This is text with an ![image](https://some-random-link-to-image.com) between the words", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://some-random-link-to-image.com"),
            TextNode(" between the words", TextType.TEXT),
        ])

    def test_singlelink(self):
        node = TextNode("This is text with a [link](https://some-random-link.com) between the words", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://some-random-link.com"),
            TextNode(" between the words", TextType.TEXT),
        ])

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes,[
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ])

    def test_split_links(self):
        node = TextNode("This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes,[
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ])

    def test_multiplenodes(self):
        node1 = TextNode("This is text with an ![image](https://some-random-link-to-image.com) between the words", TextType.TEXT)
        node2 = TextNode("This is text with a [link](https://some-random-link.com) between the words", TextType.TEXT)
        node3 = TextNode("This is text with an ![image](https://some-random-link-to-image.com) and then a [link](https://some-random-link.com) between the words", TextType.TEXT)
        new_nodes1 = split_nodes_image([node1, node2, node3])
        new_nodes2 = split_nodes_link(new_nodes1)

        self.assertEqual(new_nodes2, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://some-random-link-to-image.com"),
            TextNode(" between the words", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://some-random-link.com"),
            TextNode(" between the words", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://some-random-link-to-image.com"),
            TextNode(" and then a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://some-random-link.com"),
            TextNode(" between the words", TextType.TEXT),
        ])

    def test_imageatstart(self):
        node = TextNode("![image](https://some-random-link-to-image.com) This is text with image at the start", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("image", TextType.IMAGE, "https://some-random-link-to-image.com"),
            TextNode(" This is text with image at the start", TextType.TEXT),
        ])

    def test_imageatend(self):
        node = TextNode("This is text with image at the end ![image](https://some-random-link-to-image.com)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with image at the end ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://some-random-link-to-image.com"),
        ])

    def test_linkatstart(self):
        node = TextNode("[link](https://some-random-link.com) This is text with link at the start", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("link", TextType.LINK, "https://some-random-link.com"),
            TextNode(" This is text with link at the start", TextType.TEXT),
        ])

    def test_linkatend(self):
        node = TextNode("This is text with link at the end [link](https://some-random-link.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with link at the end ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://some-random-link.com"),
        ])

if __name__ == "__main__":
    unittest.main()
