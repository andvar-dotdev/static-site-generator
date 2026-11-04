import unittest
from md_to_html import markdown_to_html_node

class TestMdtoHTML(unittest.TestCase):
    def test_emptytext(self):
        with self.assertRaises(Exception):
            markdown_to_html_node("")

    def test_Nonetext(self):
        with self.assertRaises(Exception):
            markdown_to_html_node(None)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """# My Heading at Level 1

## Introduction at Level 2

This is **bolded** paragraph
text in a p
tag here

## Second Heading at Level 2

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>My Heading at Level 1</h1><h2>Introduction at Level 2</h2><p>This is <b>bolded</b> paragraph text in a p tag here</p><h2>Second Heading at Level 2</h2><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_quotes(self):
        md = """
>This is **bolded** paragraph quote
> text in a p
>tag here

> This is another paragraph quote with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> paragraph quote text in a p tag here</blockquote><blockquote>This is another paragraph quote with <i>italic</i> text and <code>code</code> here</blockquote></div>",
        )

    def test_ulists(self):
        md = """
- Item 1
- Item 2
- Item 3

- Item in new **bolded** list

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><ul><li>Item in new <b>bolded</b> list</li></ul></div>",
        )

    def test_olists(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
4. Item 4
5. Item 5
6. Item 6
7. Item 7
8. Item 8
9. Item 9
10. Item 10

1. Item in new **bolded** list

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li><li>Item 4</li><li>Item 5</li><li>Item 6</li><li>Item 7</li><li>Item 8</li><li>Item 9</li><li>Item 10</li></ol><ol><li>Item in new <b>bolded</b> list</li></ol></div>",
        )

    def test_combination(self):
        md = """# Header

Paragraph of
some text
in different lines.

- List item 1
- List item 2

[link](https://somewhere.com)

![image](https://imgr.com/something-about-art)

_italics_

**bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Header</h1><p>Paragraph of some text in different lines.</p><ul><li>List item 1</li><li>List item 2</li></ul><p><a href="https://somewhere.com">link</a></p><p><img src="https://imgr.com/something-about-art" alt="image"></img></p><p><i>italics</i></p><p><b>bold</b></p></div>'
        )

if __name__ == "__main__":
    unittest.main()
