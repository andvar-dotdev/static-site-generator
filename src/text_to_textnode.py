from enum import Enum
from textnode import TextNode, TextType
from splitters import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnode(text: str) -> list[TextNode]:
    if not text:
        raise Exception("Error: No text provided.")

    return split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        [TextNode(text, TextType.TEXT)], "**", TextType.BOLD,
                    ), "_", TextType.ITALIC
                ), "`", TextType.CODE,
            ),
        ),
    )

def markdown_to_blocks(markdown: str) -> list[str]:
    if not markdown:
        raise Exception("Error: No markdown text provided.")
    list_markdown: list[str] = []

    split_markdown: list[str] = markdown.split("\n\n")
    for i in range(len(split_markdown)):
        temp: str = split_markdown[i].strip()
        if not temp:
            continue
        list_markdown.append(temp)
    return list_markdown

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered list"
    O_LIST = "ordered list"

def block_to_block_type(block: str) -> BlockType:
    if not block:
        raise Exception("Error: No block markdown text provided.")
    block = block.strip()
    split_block: list[str] = block.split("\n")
    if any(split_block[0].startswith("#" * i + " ") for i in range(1, 7)):
        return BlockType.HEADING
    if split_block[0].count("```") == 1 and split_block[-1].count("```") == 1:
        return BlockType.CODE
    if all(line.startswith(">") for line in split_block):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in split_block):
        return BlockType.U_LIST
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(split_block)):
        return BlockType.O_LIST
    return BlockType.PARAGRAPH
