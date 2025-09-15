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

if __name__ == "__main__":
    unittest.main()
