
class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list["HTMLNode"] | None = children
        self.props: dict[str, str] | None = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or not self.props:
            return ""
        output: str = ''

        for key in self.props:
            output += f' {key}="{self.props[key]}"'
        return output

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None: # or not self.value
            raise ValueError(f"Error: LeafNode needs to be provided with a value! Tag is {self.tag}")
        elif self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[LeafNode | ParentNode], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or not self.tag:
            raise ValueError("Error: ParentNode needs to be provided with a tag!")
        elif self.children is None:
            raise ValueError("Error: ParentNode needs to have children!")
        else:
            output: str = f'<{self.tag}{self.props_to_html()}>'
            for child in self.children:
                output += child.to_html()
            output += f'</{self.tag}>'
        return output
