import unittest
from rhyme import Rhyme

class TestRhyme(unittest.TestCase):
    def test_get_vowel(self):
        # Basic test
        text = "さくら"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "aua")
        text = "ありがとう"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "aiaou")

    def test_yoon(self):
        # Test for yoon (e.g., じゃ, きゃ)
        text = "ちゃ"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "a")
        text = "しょ"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "o")

    def test_choon(self):
        # Test for choon (e.g., あー)
        text = "ラーメン"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "aae")
        text = "コーヒー"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "ooii")

    def test_n(self):
        # Test for 'ん'
        text = "かんたん"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "aan")
        text = "しんぶん"
        rhyme = Rhyme(text)
        self.assertEqual(rhyme.vowel, "iun")

if __name__ == "__main__":
    unittest.main()
