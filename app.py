import streamlit as st
import requests

# FastAPIサーバーのURL
BASE_URL = "http://127.0.0.1:8000"

st.title("Rhyme Generation Helper")

# --- 母音情報取得 ---
st.header("単語の母音情報を取得")
vowel_input = st.text_input("単語を入力してください", key="vowel_word")
if st.button("母音情報を取得", key="get_vowels"):
    if vowel_input:
        try:
            response = requests.get(f"{BASE_URL}/vowels/{vowel_input}")
            response.raise_for_status()  # エラーがあれば例外を発生
            st.success("母音情報:")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"APIへの接続に失敗しました: {e}")
    else:
        st.warning("単語を入力してください。")

# --- 韻の判定 ---
st.header("韻を踏んでいるか判定")
base_word_input = st.text_input("基準となる単語を入力してください", key="base_word")
target_words_input = st.text_area("判定したい単語を改行で区切って入力してください", key="target_words")

if st.button("判定する", key="check_rhymes"):
    if base_word_input and target_words_input:
        target_words = [word.strip() for word in target_words_input.split('\n') if word.strip()]
        if target_words:
            payload = {
                "base_word": base_word_input,
                "target_words": target_words
            }
            try:
                response = requests.post(f"{BASE_URL}/rhyme-check/", json=payload)
                response.raise_for_status() # エラーがあれば例外を発生
                results = response.json()
                
                st.success("判定結果:")
                for word, result in zip(target_words, results):
                    st.write(f"- `{base_word_input}` と `{word}`: {'韻を踏んでいます' if result else '韻を踏んでいません'}")

            except requests.exceptions.RequestException as e:
                st.error(f"APIへの接続に失敗しました: {e}")
        else:
            st.warning("判定したい単語を入力してください。")
    else:
        st.warning("基準となる単語と判定したい単語の両方を入力してください。")
