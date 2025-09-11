from rhyme import TextAnalyzer

def test_text_analyzer_get_vowels():
    assert TextAnalyzer("こんにちは").get_vowels() == "おいうあ"
    assert TextAnalyzer("さようなら").get_vowels() == "あおうあ"
    assert TextAnalyzer("テスト").get_vowels() == "えお"
    assert TextAnalyzer("日本語").get_vowels() == "いお"
    assert TextAnalyzer("あいうえお").get_vowels() == "あいうえお"
    assert TextAnalyzer("かきくけこ").get_vowels() == "あいうえお"
    assert TextAnalyzer("がぎぐげご").get_vowels() == "あいうえお"
    assert TextAnalyzer("パピプペポ").get_vowels() == "あいうえお"
    assert TextAnalyzer("漢字").get_vowels() == "あい"
    assert TextAnalyzer("").get_vowels() == ""
    assert TextAnalyzer("abc").get_vowels() == ""
