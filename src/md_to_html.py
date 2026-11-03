from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnode import markdown_to_blocks, BlockType, block_to_block_type, text_to_textnode

def markdown_to_html_node(markdown: str) -> ParentNode:
    if not markdown:
        raise Exception("Error: No markdown text supplied.")
    blocks: list[str] = markdown_to_blocks(markdown)
    nodes: list[LeafNode | ParentNode] = []

    for block in blocks:
        block_type: BlockType = block_to_block_type(block)
        match block_type:
            case block_type.PARAGRAPH:
                block = replace_new_lines(block)
                children: list[LeafNode | ParentNode] = text_to_children(block)
                nodes.append(ParentNode("p", children))
            case block_type.HEADING:
# Limitation in code: cases where #Heading 1\n##Heading 2 is used without two \n separating them will be missed with curent code.
# Some sort of splitting would either need to be included in this segment, or in markdown_to_blocks function.
                heading_text: str = block.lstrip("#")
                level: int = len(block) - len(heading_text)
                children = text_to_children(heading_text.lstrip())
                nodes.append(ParentNode(f"h{level}", children))
            case block_type.CODE:
                code: str = block[4:-3]
                code_node: TextNode = TextNode(code, TextType.CODE)
                code_leaf: LeafNode = text_node_to_html_node(code_node)
                nodes.append(ParentNode("pre", [code_leaf]))
            case block_type.QUOTE:
# Limitation in code: multi-line quotes are flattened into a single line, consistent with how paragraphs are handled; no <br> or line-break preservation is implemented.
                lines: list[str] = block.split("\n")
                cleaned_lines: list[str] = [line.lstrip("> ") for line in lines]
                quote_text: str = " ".join(cleaned_lines)
                children = text_to_children(quote_text)
                nodes.append(ParentNode("blockquote", children))
            case block_type.U_LIST:
                list_items: list[str] = block.split("\n")
                children = []
                for list_item in list_items:
                    children.append(ParentNode("li", text_to_children(list_item[2:])))
                nodes.append(ParentNode("ul", children))
            case block_type.O_LIST:
                list_items: list[str] = block.split("\n")
                children = []
                for list_item in list_items:
                    children.append(ParentNode("li", text_to_children(list_item[list_item.find(".") + 2:])))
                nodes.append(ParentNode("ol", children))
    return ParentNode("div", nodes)

def replace_new_lines(text: str) -> str:
    return text.replace('\n', ' ')

def text_to_children(text) -> list[LeafNode]:
    leafnodes: list[LeafNode] = []
    textnodes: list[TextNode] = text_to_textnode(text)
    for textnode in textnodes:
        leafnodes.append(text_node_to_html_node(textnode))
    return leafnodes
