from fastapi import FastAPI
from ..core.rhyme import WordInfo
from ..core.rhyme_checker import RhymeChecker
from pydantic import BaseModel
from typing import List

app = FastAPI()

class RhymeCheckRequest(BaseModel):
    base_word: str
    target_words: List[str]

@app.get("/vowels/{text}")
def get_vowels(text: str):
    rhyme = WordInfo(text)
    return rhyme.vowels

@app.post("/rhyme-check/")
def rhyme_check(request: RhymeCheckRequest):
    checker = RhymeChecker(request.base_word, request.target_words)
    return checker.results