import unittest
from scripts import readability_main


class CleanTextTestCase(unittest.TestCase):
    def test_clean_text(self):
        text = "Dr. Eeyore is nice. We love her!"
        self.assertEqual(readability_main.clean_text(text), "Dr Eeyore is nice. We love her.", "Error in cleaning text.")


class GetReadabilityScoreTestCase(unittest.TestCase):
    def test_get_readability_score(self):
        text = "The grass is green."
        self.assertEqual(readability_main.get_readability_score(text), 139.32500000000002, 'The score is off, check input.')


if __name__ == '__main__':
    unittest.main()
