import os, shutil

def main() -> None:
    initialise_public("../static", "../public")

def initialise_public(source: str, destination: str) -> None:
    if os.path.exists(source) and os.path.exists(destination):
        remove_contents(destination)
        items: list[str] = os.listdir(source)
        for item in items:
            item_path: str = os.path.join(source, item)
            #print(f"The items found are {items}. Current item is {item}, and the path checked is {item_path}")
            if os.path.isfile(item_path):
                shutil.copy(item_path, destination)
            else:
                new_destination: str = os.path.join(destination, item)
                os.mkdir(new_destination)
                initialise_public(item_path, new_destination)


def remove_contents(path: str) -> None:
    abs_path = os.path.join(__file__[:-7], path)
    abs_path = os.path.normpath(abs_path)
    shutil.rmtree(abs_path)
    os.mkdir(abs_path)

main()
