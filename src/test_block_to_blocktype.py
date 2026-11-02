import unittest
from enum import Enum
from text_to_textnode import block_to_block_type, BlockType

class TestBlocktoBlockTypes(unittest.TestCase):
    def test_emptytext(self):
        with self.assertRaises(Exception):
            block_to_block_type("")

    def test_Nonetext(self):
        with self.assertRaises(Exception):
            block_to_block_type(None)

    def test_heading_block(self):
        block: str = "# This is **bolded** heading 1"
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code_block(self):
        block: str = "```\nThis is code block\n```\n"
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote_block(self):
        block: str = """> This is **bolded** quote
> This is **bolded** quote
>This is **bolded** quote
>This is **bolded** quote"""
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_ulist_block(self):
        block: str = """- This is **bolded** unordered list
- This is **bolded** unordered list
- This is **bolded** unordered list
- This is **bolded** unordered list"""
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.U_LIST)

    def test_olist_block(self):
        block: str = """1. This is **bolded** ordered list
2. This is **bolded** ordered list
3. This is **bolded** ordered list"""
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.O_LIST)

    def test_2digit_olist_block(self):
        block: str = """1. This is **bolded** ordered list
2. This is **bolded** ordered list
3. This is **bolded** ordered list
4. This is **bolded** ordered list
5. This is **bolded** ordered list
6. This is **bolded** ordered list
7. This is **bolded** ordered list
8. This is **bolded** ordered list
9. This is **bolded** ordered list
10. This is **bolded** ordered list
11. This is **bolded** ordered list
12. This is **bolded** ordered list
13. This is **bolded** ordered list"""
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.O_LIST)


    def test_paragraph_block(self):
        block: str = "This is **bolded** paragraph block"
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraph_block_with_random_backticks(self):
        block: str = "```code` This is **bolded** ``` paragraph block]"
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_not_heading_block(self):
        block: str = "####### This is not a heading"
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_not_code_block(self):
        block: str = "```\n This is not a code block"
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_not_quote_block(self):
        block: str = """> This is a quote
> This is a quote
This is not a quote
> This is a quote"""
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_not_ulist_block(self):
        block: str = """- This is an unordered list item
- This is an unordered list item
1. This is **bolded** ordered list item
- This is an unordered list item"""
        block_type: Enum = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
