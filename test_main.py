from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_vowels():
    response = client.get("/vowels/こんにちは")
    assert response.status_code == 200
    assert response.json() == ['お', ['ん', 'う', 'optional'], 'い', ['い', 'optional'], 'あ']

def test_rhyme_check():
    response = client.post("/rhyme-check/", json={"base_word": "しんぶんし", "target_words": ["きんようび", "こんにちは"]})
    assert response.status_code == 200
    assert response.json() == [True, False]