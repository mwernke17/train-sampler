import streamlit as st
import random

st.set_page_config(page_title="Number Sampler", layout="wide")

# Initialize session state if needed
if "numbers" not in st.session_state:
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []

st.title("Random Number Sampler + Entry Grid")

# Define individual inputs in the specified order
left_column, center_column, right_column = st.columns([1, 3, 1])

with left_column:
    left_inputs = [st.text_input("", key=f"box_{i+1}", label_visibility="collapsed", max_chars=2) for i in reversed(range(5))]  # box_1 to box_5 from bottom to top

with center_column:
    top_cols = st.columns(10)
    top_inputs = [top_cols[i].text_input("", key=f"box_{i+6}", label_visibility="collapsed", max_chars=2) for i in range(10)]  # box_6 to box_15 left to right

with right_column:
    right_inputs = [st.text_input("", key=f"box_{i+16}", label_visibility="collapsed", max_chars=2) for i in range(5)]  # box_16 to box_20 from top to bottom

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
