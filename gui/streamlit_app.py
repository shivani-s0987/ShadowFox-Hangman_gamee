import streamlit as st
import random
from word_bank import words
from score_tracker import log_result, generate_score_chart

st.set_page_config(page_title="Hangman Game 🎮", layout="centered")
st.title("🎯 HANGMAN - Streamlit Edition")
st.markdown("Guess the hidden word letter-by-letter!")

# --- Session Setup ---
if "word" not in st.session_state:
    st.session_state.word, st.session_state.hint = random.choice(list(words.items()))
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.guessed_letters = set()
    st.session_state.attempts_left = 6
    st.session_state.game_over = False
    st.session_state.status = ""

# --- Display Word & Hint ---
st.markdown(f"💡 **Hint**: `{st.session_state.hint}`")
display_word = " ".join([l if l in st.session_state.guessed_letters else "_" for l in st.session_state.word])
st.markdown(f"🔤 Word: `{display_word}`")

# --- Game Logic ---
if not st.session_state.game_over:
    guess = st.text_input("📥 Enter a letter:", max_chars=1).strip().lower()

    if st.button("✅ Submit Guess") and guess:
        if not guess.isalpha():
            st.warning("❗ Please enter a valid letter.")
        elif guess in st.session_state.guessed_letters:
            st.warning("⚠️ You already guessed that letter.")
        elif guess in st.session_state.word_letters:
            st.session_state.guessed_letters.add(guess)
            st.session_state.word_letters.remove(guess)
        else:
            st.session_state.guessed_letters.add(guess)
            st.session_state.attempts_left -= 1

        # --- Win or Lose Check ---
        if not st.session_state.word_letters:
            st.success(f"🎉 YOU WON! Word was: {st.session_state.word}")
            st.session_state.status = "WIN"
            st.session_state.game_over = True
        elif st.session_state.attempts_left == 0:
            st.error(f"💀 YOU LOST! Word was: {st.session_state.word}")
            st.session_state.status = "LOSE"
            st.session_state.game_over = True

# --- Show Attempts Left ---
st.info(f"❤️ Attempts Left: `{st.session_state.attempts_left}`")

# --- End Game: Show Chart + Restart Option ---
if st.session_state.game_over:
    log_result(st.session_state.status, st.session_state.word)  # ✅ Fixed order
    generate_score_chart()
    st.image("charts/score_summary.png", caption="📊 Score Summary")

    if st.button("🔁 Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
