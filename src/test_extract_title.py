import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        md: str = "# Heading 1"
        self.assertEqual(extract_title(md), "Heading 1")

    def test_title_not_in_first_line(self):
        md: str = """ Som random text.

Gibberish kl;jasdhflikajusdhfalsikedjufh
## Different level heading

# Heading 1

###End
"""
        self.assertEqual(extract_title(md), "Heading 1")

    def test_title_with_many_spaces(self):
        md: str = "# Heading 1              "
        self.assertEqual(extract_title(md), "Heading 1")

if __name__ == "__main__":
    unittest.main()
