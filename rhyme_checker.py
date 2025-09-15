from rhyme import WordInfo

class RhymeChecker:
    def __init__(self, base_word, target_words):
        self.base_word = WordInfo(base_word)
        if isinstance(target_words, str):
            self.target_words = [WordInfo(target_words)]
        else:
            self.target_words = [WordInfo(word) for word in target_words]
        self.results = self._check_rhymes()

    def _check_rhymes(self):
        results = []
        for target_word in self.target_words:
            if self.base_word.vowels == target_word.vowels:
                results.append(True)
            else:
                results.append(False)
        return results
