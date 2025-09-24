from rhyme import WordInfo

class RhymeChecker:
    def __init__(self, base_word, target_words):
        self.base_word_info = WordInfo(base_word)
        if isinstance(target_words, str):
            self.target_words_info = [WordInfo(target_words)]
        else:
            self.target_words_info = [WordInfo(word) for word in target_words]
        self.results = self._check_rhymes()

    def _flatten_vowels(self, vowels):
        flat_vowels = []
        for vowel in vowels:
            if not isinstance(vowel, list):
                flat_vowels.append(vowel)
        return flat_vowels

    def _check_rhymes(self):
        results = []
        base_vowels = self._flatten_vowels(self.base_word_info.vowels)
        for target_word_info in self.target_words_info:
            target_vowels = self._flatten_vowels(target_word_info.vowels)

            if not base_vowels or not target_vowels:
                results.append(False)
                continue

            # 後方からマッチング
            i = len(base_vowels) - 1
            j = len(target_vowels) - 1
            match_count = 0

            while i >= 0 and j >= 0:
                if base_vowels[i] == target_vowels[j]:
                    match_count += 1
                else:
                    break
                i -= 1
                j -= 1

            # 母音の半分以上が一致しているか
            results.append(match_count >= len(base_vowels) / 2)
        return results
