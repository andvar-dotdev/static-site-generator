import os, shutil, sys
from htmlnode import ParentNode
from md_to_html import markdown_to_html_node

def main() -> None:
    # Note: limit of code is the way the slicing is used and relative paths. If main.py is not ran from root of project, or is renamed, or is ran in Windows, the below will not work.
    initialise_public("./static", "./docs")
    generate_page_recursive("./content", "./template.html", "./docs", basepath)

def initialise_public(source: str, destination: str) -> None:
    if not os.path.exists(destination):
        os.mkdir(destination)
    if os.path.exists(source):
        remove_contents(destination)
        items: list[str] = os.listdir(source)
        for item in items:
            item_path: str = os.path.join(source, item)
            if os.path.isfile(item_path):
                shutil.copy(item_path, destination)
            else:
                new_destination: str = os.path.join(destination, item)
                os.mkdir(new_destination)
                initialise_public(item_path, new_destination)

def remove_contents(path: str) -> None:
    abs_path = os.path.join(__file__[:-11], path)
    abs_path = os.path.normpath(abs_path)
    shutil.rmtree(abs_path)
    os.mkdir(abs_path)

def extract_title(markdown: str) -> str:
    if not markdown:
        raise Exception("Error: No markdown provided.")
    md_split: list[str] = markdown.split("\n")
    for line in md_split:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("Error: No h1 header found, no title provided to the document.")

def generate_page_recursive(from_path: str, template_path: str, dest_path: str, basepath: str | None=None) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    items: list[str] = os.listdir(from_path)
    for item in items:
        item_path: str = os.path.join(from_path, item)
#        print(f"current item is {item} and the path is {item_path}. Is this a file? {os.path.isfile(item_path)}")
        if os.path.isfile(item_path):
            with open(item_path) as f:
                md: str = f.read()
            with open(template_path) as f:
                template: str = f.read()
            html_node: ParentNode = markdown_to_html_node(md)
            html_string: str = html_node.to_html()
            title: str = extract_title(md)
            html_page: str = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
            with open(os.path.join(dest_path, "index.html"), "x") as f:
                f.write(html_page)
        else:
            new_destination: str = os.path.join(dest_path, item)
            os.mkdir(new_destination)
            generate_page_recursive(item_path, template_path, new_destination, basepath)

basepath: str = sys.argv[1]
main()
