# Rhyme Generation

## ディレクトリ構成
```
rhyme_generation/
├── __init__.py
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── test_main.py
├── core/
│   ├── __init__.py
│   ├── rhyme.py
│   ├── rhyme_checker.py
│   ├── test_rhyme.py
│   └── test_rhyme_checker.py
└── web/
    ├── __init__.py
    └── app.py

requirements.txt
debug_kakasi.py
```

## FastAPI の起動
```bash
uvicorn rhyme_generation.api.main:app --reload
```

## Streamlit の起動
```bash
streamlit run rhyme_generation/web/app.py
```
