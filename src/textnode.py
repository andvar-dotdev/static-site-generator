from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: "TextType", url: str | None=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: "TextNode") -> bool:
        return True if self.text == other.text and self.text_type == other.text_type and self.url == other.url else False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case text_node.text_type.TEXT:
            return LeafNode(None, text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode("b", text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode("i", text_node.text)
        case text_node.text_type.CODE:
            return LeafNode("code", text_node.text)
        case text_node.text_type.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case text_node.text_type.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Error: TextNode uses a TextType that is not implemented.")
