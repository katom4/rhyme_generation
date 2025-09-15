import unittest
from rhyme import WordInfo

class TestWordInfo(unittest.TestCase):
    def test_get_vowels_hiragana(self):
        word_info = WordInfo("こんにちは")
        self.assertEqual(word_info.vowels, "おんいいあ")

    def test_get_vowels_kanji(self):
        word_info = WordInfo("日本語")
        self.assertEqual(word_info.vowels, "いおんお")

    def test_get_vowels_katakana(self):
        word_info = WordInfo("コンピュータ")
        self.assertEqual(word_info.vowels, "おんううあ")

if __name__ == '__main__':
    unittest.main()