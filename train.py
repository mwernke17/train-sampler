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
    if st.button("Draw Next Number"):
        next_number = st.session_state.numbers.pop()
        st.session_state.sampled.append(next_number)
        st.session_state.last_drawn_index = len(st.session_state.sampled)
        st.success(f"Next number: {next_number}")
else:
    if len(st.session_state.sampled) >= 20:
        st.warning("20 numbers drawn. Press below to reset.")
    elif st.session_state.last_drawn_index > len([i for i in range(1, 21) if st.session_state.get(f"box_{i}")]):
        st.info("Please place the last number before drawing the next.")

# Display sampled so far
if st.session_state.sampled:
    st.info("Numbers drawn so far: " + ", ".join(map(str, st.session_state.sampled)))

# Reset button
if st.button("Reset Sampling"):
    st.session_state.reset_flag = True
    st.experimental_rerun()

st.divider()
st.subheader("Enter Your Numbers")

input_positions = {
    (4, 0): 1,
    (3, 0): 2,
    (2, 0): 3,
    (1, 0): 4,
    (0, 0): 5,
    (0, 1): 6,
    (0, 2): 7,
    (0, 3): 8,
    (0, 4): 9,
    (0, 5): 10,
    (0, 6): 11,
    (0, 7): 12,
    (0, 8): 13,
    (0, 9): 14,
    (0, 10): 15,
    (0, 11): 16,
    (1, 11): 17,
    (2, 11): 18,
    (3, 11): 19,
    (4, 11): 20,
}

for row in range(5):
    cols = st.columns(12)
    for col in range(12):
        index = input_positions.get((row, col))
        if index:
            disabled = f"box_{index}" in st.session_state and st.session_state[f"box_{index}"] != ""
            if st.button(f"Input {index}", key=f"btn_{index}", use_container_width=True):
                if not disabled and len(st.session_state.sampled) >= index:
                    st.session_state[f"box_{index}"] = str(st.session_state.sampled[index - 1])
                    st.session_state.last_drawn_index = index  # allow next draw
            cols[col].text_input(
                "",
                key=f"box_{index}",
                label_visibility="collapsed",
                disabled=disabled,
                placeholder=""
            )
        else:
            cols[col].markdown(" ")  # empty cell

st.markdown("""
    <style>
        input[type="text"] {
            width: 100px !important;
            height: 100px !important;
            text-align: center !important;
            font-size: 22px !important;
        }
        button[kind="secondary"] {
            font-size: 12px;
            padding: 2px 0;
        }
    </style>
""", unsafe_allow_html=True)
