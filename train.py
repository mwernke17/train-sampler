import streamlit as st
import random

st.set_page_config(page_title="Number Sampler", layout="wide")

# Initialize session state if needed
if "numbers" not in st.session_state:
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []

st.title("Random Number Sampler")

# Fixed train logo reference from original version
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Steam_locomotive_icon.svg/120px-Steam_locomotive_icon.svg.png", width=100)

st.subheader("Random Sampler")
if len(st.session_state.sampled) < 20:
    if st.button("Draw Next Number"):
        next_number = st.session_state.numbers.pop()
        st.session_state.sampled.append(next_number)
        st.success(f"Next number: {next_number}")
else:
    st.warning("20 numbers drawn. Press below to reset.")

if st.session_state.sampled:
    st.info("Numbers drawn so far: " + ", ".join(map(str, st.session_state.sampled)))

if st.button("Reset Sampling"):
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""

st.divider()

st.subheader("Enter Your Numbers")

# Define individual inputs in the specified order
left_column, center_column, right_column = st.columns([1, 3, 1])

with left_column:
    for i in reversed(range(5)):
        st.text_input("", key=f"box_{i+1}", label_visibility="collapsed", max_chars=2, placeholder="")

with center_column:
    top_cols = st.columns(10)
    for i in range(10):
        top_cols[i].text_input("", key=f"box_{i+6}", label_visibility="collapsed", max_chars=2, placeholder="")

with right_column:
    for i in range(5):
        st.text_input("", key=f"box_{i+16}", label_visibility="collapsed", max_chars=2, placeholder="")

# Apply consistent size using CSS
st.markdown("""
    <style>
        input[type="text"] {
            width: 75px !important;
            height: 75px !important;
            text-align: center !important;
            font-size: 20px !important;
        }
    </style>
""", unsafe_allow_html=True)
