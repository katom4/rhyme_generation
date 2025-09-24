from pykakasi import kakasi

class WordInfo:
    def __init__(self, word):
        self.word = word
        self.kks = kakasi()
        self._update_vowels()

    def _extract_basic_units(self, hira):
        hiragana_vowels = {
            'あ': 'あ', 'い': 'い', 'う': 'う', 'え': 'え', 'お': 'お',
            'か': 'あ', 'き': 'い', 'く': 'う', 'け': 'え', 'こ': 'お',
            'さ': 'あ', 'し': 'い', 'す': 'う', 'せ': 'え', 'そ': 'お',
            'た': 'あ', 'ち': 'い', 'つ': 'う', 'て': 'え', 'と': 'お',
            'な': 'あ', 'に': 'い', 'ぬ': 'う', 'ね': 'え', 'の': 'お',
            'は': 'あ', 'ひ': 'い', 'ふ': 'う', 'へ': 'え', 'ほ': 'お',
            'ま': 'あ', 'み': 'い', 'む': 'う', 'め': 'え', 'も': 'お',
            'や': 'あ', 'ゆ': 'う', 'よ': 'お',
            'ら': 'あ', 'り': 'い', 'る': 'う', 'れ': 'え', 'ろ': 'お',
            'わ': 'あ', 'を': 'お',
            'ん': 'ん',
            'が': 'あ', 'ぎ': 'い', 'ぐ': 'う', 'げ': 'え', 'ご': 'お',
            'ざ': 'あ', 'じ': 'い', 'ず': 'う', 'ぜ': 'え', 'ぞ': 'お',
            'だ': 'あ', 'ぢ': 'い', 'づ': 'う', 'で': 'え', 'ど': 'お',
            'ば': 'あ', 'び': 'い', 'ぶ': 'う', 'べ': 'え', 'ぼ': 'お',
            'ぱ': 'あ', 'ぴ': 'い', 'ぷ': 'う', 'ぺ': 'え', 'ぽ': 'お',
        }
        small_vowels = {'ゃ': 'あ', 'ゅ': 'う', 'ょ': 'お', 'ぁ': 'あ', 'ぃ': 'い', 'ぅ': 'う', 'ぇ': 'え', 'ぉ': 'お'}

        basic_units = []
        i = 0
        while i < len(hira):
            char = hira[i]

            if char == 'ー':
                basic_units.append('ー')
                i += 1
            elif char == 'っ':
                basic_units.append('っ')
                i += 1
            elif char == 'ん':
                basic_units.append('ん')
                i += 1
            elif i + 1 < len(hira) and hira[i+1] in small_vowels:
                basic_units.append(small_vowels[hira[i+1]])
                i += 2
            elif char in hiragana_vowels:
                basic_units.append(hiragana_vowels[char])
                i += 1
            else:
                i += 1  # Skip non-vowel characters
        return basic_units

    def _process_units_with_optional_logic(self, basic_units):
        final_vowels = []
        last_simple_vowel = None
        consecutive_count = 0

        for unit in basic_units:
            if unit == 'ー':
                if final_vowels and last_simple_vowel: # Only if there was a previous simple vowel
                    # Find the last entry in final_vowels that corresponds to last_simple_vowel
                    # and modify it to be optional.
                    if not isinstance(final_vowels[-1], list):
                        final_vowels[-1] = [final_vowels[-1], 'optional']
                    elif final_vowels[-1] and final_vowels[-1][0] == last_simple_vowel:
                        # If it's already an optional list of the same vowel, no change needed
                        pass
                # Reset consecutive count for simple vowels after special marker
                last_simple_vowel = None
                consecutive_count = 0
            elif unit == 'っ':
                final_vowels.append(['っ', 'optional'])
                last_simple_vowel = None
                consecutive_count = 0
            elif unit == 'ん':
                final_vowels.append(['ん', 'う', 'optional'])
                last_simple_vowel = None
                consecutive_count = 0
            else:  # It's a simple vowel
                if last_simple_vowel == unit and consecutive_count == 1:
                    final_vowels.append([unit, 'optional'])
                    consecutive_count += 1  # Now 2 consecutive, next won't be optional
                else:
                    final_vowels.append(unit)
                    last_simple_vowel = unit
                    consecutive_count = 1
        return final_vowels

    def _update_vowels(self):
        result = self.kks.convert(self.word)
        hiragana = "".join([item['hira'] for item in result])
        basic_units = self._extract_basic_units(hiragana)
        self.vowels = self._process_units_with_optional_logic(basic_units)