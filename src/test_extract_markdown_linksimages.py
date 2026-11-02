import unittest
from splitters import extract_markdown_images, extract_markdown_links

class TestExtractImageLink(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://some-website.com)"
        )
        self.assertListEqual([("link", "https://some-website.com")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a second style of inage with more text ![I love this inmage because it is an image.](https://i.imgur.com/zjjcdfsfdsfsdKZ.png), and a third image with its link as alt text ![http://i.imgur.com/zjjcdfsafasdfaw3erfJKZ.png](http://i.imgur.com/zjjcdfsafasdfaw3erfJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("I love this inmage because it is an image.", "https://i.imgur.com/zjjcdfsfdsfsdKZ.png"), ("http://i.imgur.com/zjjcdfsafasdfaw3erfJKZ.png", "http://i.imgur.com/zjjcdfsafasdfaw3erfJKZ.png")], matches)

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://some-website.com), a second style of link with more text [Follow this link to my of sweetie!](http://some-scammer-virus-website.com), and a third link with its link as text ![https://some-website.com](https://some-website.com)"
        )
        self.assertListEqual([("link", "https://some-website.com"), ("Follow this link to my of sweetie!", "http://some-scammer-virus-website.com"), ("https://some-website.com", "https://some-website.com")], matches)

if __name__ == "__main__":
    unittest.main()
