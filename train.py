import streamlit as st
import random

st.set_page_config(page_title="Number Sampler", layout="wide")

# Initialize session state if needed
if "numbers" not in st.session_state:
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []

st.title("Random Number Sampler + Entry Grid")

# Layout for the arrow path and input boxes
left_column, center_column, right_column = st.columns([1, 3, 1])

with left_column:
    st.markdown("### Left Side")
    left_inputs = [st.text_input("", key=f"left_{i}", label_visibility="collapsed") for i in range(5)]

with center_column:
    st.markdown("### Top Row")
    top_cols = st.columns(10)
    top_inputs = [top_cols[i].text_input("", key=f"top_{i}", label_visibility="collapsed") for i in range(10)]
    st.markdown("""
    <div style='text-align: center;'>
    ⬆️<br>
    ⬆️<br>
    ⬆️<br>
    ⬆️<br>
    ⬆️<br>
    ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️ ➡️<br>
    ⬇️<br>
    ⬇️<br>
    ⬇️<br>
    ⬇️<br>
    ⬇️
    </div>
    """, unsafe_allow_html=True)

with right_column:
    st.markdown("### Right Side")
    right_inputs = [st.text_input("", key=f"right_{i}", label_visibility="collapsed") for i in range(5)]

st.divider()

# Sampling logic
st.subheader("Random Sampler")
if len(st.session_state.sampled) < 20:
    if st.button("Draw Next Number"):
        next_number = st.session_state.numbers.pop()
        st.session_state.sampled.append(next_number)
        st.success(f"Next number: {next_number}")
else:
    st.warning("20 numbers drawn. Press below to reset.")

if st.button("Reset Sampling"):
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []
