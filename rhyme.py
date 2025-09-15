
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
            if char == 'ー' and result:
                result.append(result[-1])
                i += 1
            elif i + 1 < len(hira) and hira[i+1] in small_vowels:
                result.append(small_vowels[hira[i+1]])
                i += 2
            elif char in hiragana_vowels:
                result.append(hiragana_vowels[char])
                i += 1
            else:
                i += 1
        return "".join(result)

    def _update_vowels(self):
        result = self.kks.convert(self.word)
        hiragana = "".join([item['hira'] for item in result])
        self.vowels = self._get_vowels_from_hiragana(hiragana)
