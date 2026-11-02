import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if not old_nodes:
        return []
    if delimiter == "":
        raise Exception("Error: No delimiter specified!")
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text: list[str] = node.text.split(delimiter)
        if len(text) % 2 == 0:
            raise Exception(f"Error: Invalid Markdown syntax, second delimeter not found in node {node}.")

        for i in range(len(text)):
            if not text[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text[i], node.text_type))
            else:
                new_nodes.append(TextNode(text[i], text_type))
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        return[]
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted: list[tuple[str, str]] = extract_markdown_images(node.text)
        if not extracted:
            new_nodes.append(node)
            continue
        text: str = node.text
        for i in range(len(extracted)):
            image_alt: str = extracted[i][0]
            image_link: str = extracted[i][1]
            split_text: list[str] = text.split(f"![{image_alt}]({image_link})", 1)
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            if i == len(extracted) - 1:
                if split_text[1]:
                    new_nodes.append(TextNode(split_text[1], TextType.TEXT))
            else:
                text = split_text[1]
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    if not old_nodes:
        return[]
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted: list[tuple[str, str]] = extract_markdown_links(node.text)
        if not extracted:
            new_nodes.append(node)
            continue
        text: str = node.text
        for i in range(len(extracted)):
            link_text: str = extracted[i][0]
            link_address: str = extracted[i][1]
            split_text: list[str] = text.split(f"[{link_text}]({link_address})", 1)
            if split_text[0]:
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_address))
            if i == len(extracted) - 1:
                if split_text[1]:
                    new_nodes.append(TextNode(split_text[1], TextType.TEXT))
            else:
                text = split_text[1]
    return new_nodes
