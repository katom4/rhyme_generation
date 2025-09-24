from pykakasi import kakasi

class WordInfo:
    def __init__(self, word):
        self.word = word
        self.kks = kakasi()
        self._update_vowels()

    def _get_vowels_from_hiragana(self, hira):
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
        small_vowels = {'ゃ': 'あ', 'ゅ': 'う', 'ょ': 'お'}
        result = []
        i = 0
        while i < len(hira):
            char = hira[i]
            vowel = None

            if char == 'ー':
                if result:
                    last_vowel_info = result[-1]
                    
                    last_vowels = []
                    if isinstance(last_vowel_info, list):
                        for item in last_vowel_info:
                            if item not in ['optional', 'っ']:
                                last_vowels.append(item)
                    else:
                        last_vowels.append(last_vowel_info)

                    if last_vowels:
                        result.append(last_vowels + ['optional'])
                i += 1
                continue

            if char == 'っ':
                if result:
                    last_vowel_info = result[-1]

                    last_vowels = []
                    if isinstance(last_vowel_info, list):
                        for item in last_vowel_info:
                            if item not in ['optional', 'っ']:
                                last_vowels.append(item)
                    else:
                        last_vowels.append(last_vowel_info)
                        
                    if last_vowels:
                        result.append(last_vowels + ['っ', 'optional'])
                else:
                    result.append(['っ', 'optional'])
                i += 1
                continue

            if char == 'ん':
                result.append(['ん', 'う', 'optional'])
                i += 1
                continue

            if i + 1 < len(hira) and hira[i+1] in small_vowels:
                vowel = small_vowels[hira[i+1]]
                i += 2
            elif char in hiragana_vowels:
                vowel = hiragana_vowels[char]
                i += 1
            else:
                i += 1
                continue

            if result:
                last_vowel_info = result[-1]
                
                last_vowels = []
                if isinstance(last_vowel_info, list):
                    for item in last_vowel_info:
                        if item not in ['optional', 'っ']:
                            last_vowels.append(item)
                else:
                    last_vowels.append(last_vowel_info)

                is_vowel_char = char in ['あ', 'い', 'う', 'え', 'お']

                if vowel in last_vowels and (is_vowel_char or len(last_vowels) == 1):
                    result.append([vowel, 'optional'])
                else:
                    result.append(vowel)
            else:
                result.append(vowel)
        return result

    def _update_vowels(self):
        result = self.kks.convert(self.word)
        hiragana = "".join([item['hira'] for item in result])
        self.vowels = self._get_vowels_from_hiragana(hiragana)
