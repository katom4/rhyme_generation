import unittest
from rhyme import WordInfo

class TestWordInfo(unittest.TestCase):
    def test_get_vowels_hiragana(self):
        word_info = WordInfo("こんにちは")
        self.assertEqual(word_info.vowels, ['お', ['ん', 'う', 'optional'], 'い', ['い', 'optional'], 'あ'])

    def test_get_vowels_kanji(self):
        word_info = WordInfo("日本語")
        self.assertEqual(word_info.vowels, ['い', 'お', ['ん', 'う', 'optional'], 'お'])

    def test_get_vowels_katakana(self):
        word_info = WordInfo("コンピュータ")
        self.assertEqual(word_info.vowels, ['お', ['ん', 'う', 'optional'], ['う', 'optional'], 'あ'])

    def test_get_vowels_art(self):
        word_info = WordInfo("アート")
        self.assertEqual(word_info.vowels, [['あ', 'optional'], 'お'])

    def test_get_vowels_matt(self):
        word_info = WordInfo("マット")
        self.assertEqual(word_info.vowels, ['あ', ['っ', 'optional'], 'お'])

    def test_get_vowels_bant(self):
        word_info = WordInfo("バント")
        self.assertEqual(word_info.vowels, ['あ', ['ん', 'う', 'optional'], 'お'])

    def test_get_vowels_pasokon(self):
        word_info = WordInfo("パソコン")
        self.assertEqual(word_info.vowels, ['あ', 'お', ['お', 'optional'], ['ん', 'う', 'optional']])

    def test_get_vowels_anun(self):
        word_info = WordInfo("あんうん")
        self.assertEqual(word_info.vowels, ['あ', ['ん', 'う', 'optional'], 'う', ['ん', 'う', 'optional']])

    def test_get_vowels_n_bar(self):
        word_info = WordInfo("んー")
        self.assertEqual(word_info.vowels, [['ん', 'う', 'optional']])

    def test_get_vowels_aka(self):
        word_info = WordInfo("あか")
        self.assertEqual(word_info.vowels, ['あ', ['あ', 'optional']])

    def test_get_vowels_abara(self):
        word_info = WordInfo("あばら")
        self.assertEqual(word_info.vowels, ['あ', ['あ', 'optional'], 'あ'])

    def test_get_vowels_katakana_example(self):
        word_info = WordInfo("カタカナ")
        self.assertEqual(word_info.vowels, ['あ', ['あ', 'optional'], 'あ', ['あ', 'optional']])

    def test_get_vowels_aaa(self):
        word_info = WordInfo("あああ")
        self.assertEqual(word_info.vowels, ['あ', ['あ', 'optional'], 'あ'])

if __name__ == '__main__':
    unittest.main()