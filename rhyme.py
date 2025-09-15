import pykakasi

class Rhyme:
    def __init__(self, text):
        self.text = text
        self.vowel = self._get_vowel()

    def _get_vowel(self):
        kks = pykakasi.kakasi()
        result = kks.convert(self.text)
        romaji = result[0]['hepburn']
        vowels = ""
        for char in romaji:
            if char in "aiueo":
                vowels += char
        
        if self.text.endswith('ん'):
            vowels += 'n'
            
        return vowels
