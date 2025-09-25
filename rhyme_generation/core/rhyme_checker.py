from .rhyme import WordInfo
from functools import lru_cache

class RhymeChecker:
    def __init__(self, base_word, target_words):
        self.base_word_info = WordInfo(base_word)
        if isinstance(target_words, str):
            self.target_words_info = [WordInfo(target_words)]
        else:
            self.target_words_info = [WordInfo(word) for word in target_words]
        self.results = self._check_rhymes()

    def _check_rhymes(self):
        results = []
        for target_word_info in self.target_words_info:
            
            @lru_cache(maxsize=None)
            def are_rhyming(base_vowel_idx, target_vowel_idx):
                if base_vowel_idx < 0 and target_vowel_idx < 0:
                    return True
                
                if base_vowel_idx < 0:
                    return all(
                        'optional' in (target_vowel if isinstance(target_vowel, list) else [target_vowel])
                        for target_vowel in target_word_info.vowels[:target_vowel_idx + 1]
                    )
                if target_vowel_idx < 0:
                    return all(
                        'optional' in (base_vowel if isinstance(base_vowel, list) else [base_vowel])
                        for base_vowel in self.base_word_info.vowels[:base_vowel_idx + 1]
                    )

                base_vowel = self.base_word_info.vowels[base_vowel_idx]
                target_vowel = target_word_info.vowels[target_vowel_idx]

                base_vowel_options = base_vowel if isinstance(base_vowel, list) else [base_vowel]
                target_vowel_options = target_vowel if isinstance(target_vowel, list) else [target_vowel]

                # Case 1: Match current vowels and move both pointers
                common_vowels = set(base_vowel_options) & set(target_vowel_options)
                if 'optional' in common_vowels:
                    common_vowels.remove('optional')

                if common_vowels and are_rhyming(base_vowel_idx - 1, target_vowel_idx - 1):
                    return True

                # Case 2: Base vowel is optional, skip it
                if 'optional' in base_vowel_options and are_rhyming(base_vowel_idx - 1, target_vowel_idx):
                    return True

                # Case 3: Target vowel is optional, skip it
                if 'optional' in target_vowel_options and are_rhyming(base_vowel_idx, target_vowel_idx - 1):
                    return True
                
                return False

            results.append(are_rhyming(len(self.base_word_info.vowels) - 1, len(target_word_info.vowels) - 1))
        return results