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
        self.scores = self._calculate_scores()

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

    def _generate_vowel_sequences(self, vowels):
        sequences = [()]
        for vowel in vowels:
            if isinstance(vowel, list):
                options = [option for option in vowel if option != 'optional']
                include_optional = 'optional' in vowel
            else:
                options = [vowel]
                include_optional = False
            next_sequences = []
            for sequence in sequences:
                for option in options:
                    next_sequences.append(sequence + (option,))
                if include_optional:
                    next_sequences.append(sequence)
            sequences = next_sequences
        unique_sequences = []
        seen = set()
        for sequence in sequences:
            if sequence not in seen:
                seen.add(sequence)
                unique_sequences.append(list(sequence))
        if not unique_sequences:
            unique_sequences.append([])
        return unique_sequences

    def _levenshtein_distance(self, first, second):
        first_length = len(first)
        second_length = len(second)
        dp = [[0] * (second_length + 1) for _ in range(first_length + 1)]
        for i in range(first_length + 1):
            dp[i][0] = i
        for j in range(second_length + 1):
            dp[0][j] = j
        for i in range(1, first_length + 1):
            for j in range(1, second_length + 1):
                cost = 0 if first[i - 1] == second[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + cost,
                )
        return dp[first_length][second_length]

    def _calculate_min_score(self, base_sequences, target_sequences, base_length, target_length, denominator):
        min_score = float("inf")
        for base_sequence in base_sequences:
            base_skip = base_length - len(base_sequence)
            for target_sequence in target_sequences:
                target_skip = target_length - len(target_sequence)
                distance = self._levenshtein_distance(base_sequence, target_sequence)
                cost = distance + 0.5 * (base_skip + target_skip)
                score = cost / denominator
                if score < min_score:
                    min_score = score
        if min_score == float("inf"):
            return 0.0
        return min_score

    def _calculate_scores(self):
        base_sequences = self._generate_vowel_sequences(self.base_word_info.vowels)
        base_length = len(self.base_word_info.vowels)
        scores = []
        for target_word_info in self.target_words_info:
            target_sequences = self._generate_vowel_sequences(target_word_info.vowels)
            target_length = len(target_word_info.vowels)
            denominator = max(base_length, target_length)
            if denominator == 0:
                scores.append(0.0)
                continue
            score = self._calculate_min_score(
                base_sequences,
                target_sequences,
                base_length,
                target_length,
                denominator,
            )
            scores.append(score)
        return scores

