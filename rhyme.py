import pykakasi

class Rhyme:
    def __init__(self, text):
        self.text = text
        self.vowel = self._get_vowel()

    def _get_vowel(self):
        kks = pykakasi.kakasi()
        result = kks.convert(self.text)
        vowels = ""
        for item in result:
            for char in item['hepburn']:
                if char in "aiueo":
                    vowels += char
        return vowels