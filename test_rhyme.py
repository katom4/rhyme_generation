import unittest
from rhyme import Rhyme

class TestRhyme(unittest.TestCase):
    def test_get_vowel(self):
        text = "さくら"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "aua")

if __name__ == "__main__":
    unittest.main()