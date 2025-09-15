import unittest
from rhyme_checker import RhymeChecker

class TestRhymeChecker(unittest.TestCase):
    def test_rhyme_checker_with_list(self):
        base_word = "いのち"
        target_words = ["みのり", "ほのお", "いおり"]
        checker = RhymeChecker(base_word, target_words)
        self.assertEqual(checker.results, [True, False, True])

    def test_rhyme_checker_with_single_word(self):
        base_word = "いのち"
        target_word = "いおり"
        checker = RhymeChecker(base_word, target_word)
        self.assertEqual(checker.results, [True])

    def test_rhyme_checker_palatalized_sounds(self):
        # Test for "じゃ"
        base_word = "じゃ"
        target_word = "いあ"
        checker = RhymeChecker(base_word, target_word)
        self.assertEqual(checker.results, [True])

        # Test for "ぴゃ"
        base_word = "ぴゃ"
        target_word = "いあ"
        checker = RhymeChecker(base_word, target_word)
        self.assertEqual(checker.results, [True])

    def test_rhyme_checker_long_vowels(self):
        # Test for "ー" (long 'a')
        base_word = "カー"
        target_word = "ああ"
        checker = RhymeChecker(base_word, target_word)
        self.assertEqual(checker.results, [True])

        # Test for "ー" (long 'i')
        base_word = "キー"
        target_word = "いい"
        checker = RhymeChecker(base_word, target_word)
        self.assertEqual(checker.results, [True])

if __name__ == "__main__":
    unittest.main()
