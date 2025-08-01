import streamlit as st
import random

st.set_page_config(page_title="Number Sampler", layout="wide")

# Handle reset with a flag
if "reset_flag" not in st.session_state:
    st.session_state.reset_flag = False

if st.session_state.reset_flag:
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
    st.session_state.reset_flag = False
    st.session_state.last_drawn_index = 0

# Initialize if missing
if "numbers" not in st.session_state:
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []
    st.session_state.last_drawn_index = 0

st.title("Random Number Sampler")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Steam_locomotive_icon.svg/120px-Steam_locomotive_icon.svg.png", width=100)

st.subheader("Random Sampler")

# Determine if we can draw a new number
allow_draw = (
    len(st.session_state.sampled) < 20 and 
    st.session_state.last_drawn_index == len(st.session_state.sampled)
)

if allow_draw:
    if st.bu
