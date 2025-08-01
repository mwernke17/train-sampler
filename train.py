import streamlit as st
import random

st.set_page_config(page_title="Number Sampler", layout="wide")

# Initialize session state if needed
if "numbers" not in st.session_state:
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15,
                                                    16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []

st.title("Random Number Sampler")

# Train logo near the top
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Steam_locomotive_icon.svg",
    width=120,
    output_format="PNG"
)

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
    st.session_state.numbers = list(range(1, 11)) + [11, 11, 12, 12, 13, 13, 14, 14, 15, 15,
                                                    16, 16, 17, 17, 18, 18, 19, 19] + list(range(20, 31))
    random.shuffle(st.session_state.numbers)
    st.session_state.sampled = []

st.divider()

st.subheader("Enter Your Numbers")

# Define individual inputs in the specified order with columns sized for spacing
left_col, center_col, right_col = st.columns([1, 7, 1])

with left_col:
    # boxes 1 to 5 (bottom to top)
    for i in reversed(range(5)):
        st.text_input("", key=f"box_{i+1}", label_visibility="collapsed", max_chars=2,
                      placeholder="", help=f"Box {i+1}")

with center_col:
    # boxes 6 to 15 across the top
    top_cols = st.columns(10)
    for i in range(10):
        top_cols[i].text_input("", key=f"box_{i+6}", label_visibility="collapsed", max_chars=2,
                               placeholder="", help=f"Box {i+6}")

with right_col:
    # boxes 16 to 20 (top to bottom)
    for i in range(5):
        st.text_input("", key=f"box_{i+16}", label_visibility="collapsed", max_chars=2,
                      placeholder="", help=f"Box {i+16}")

# CSS for uniform input box size and spacing
st.markdown("""
    <style>
        div[data-testid="stTextInput"] input {
            width: 75px !important;
            min-width: 75px !important;
            max-width: 75px !important;
            height: 50px !important;
            font-size: 20px !important;
            text-align: center !important;
            padding: 0 6px !important;
            margin: 0 4px 8px 4px !important;  /* Adds horizontal and bottom margin */
            box-sizing: border-box !important;
        }
        div[data-testid="stTextInput"] {
            min-width: 75px !important;
            max-width: 75px !important;
            margin: 0 4px !important;  /* Adds spacing around container */
        }
        /* Prevent columns from shrinking too small */
        .css-1lcbmhc.e1fqkh3o3 {
            min-width: 80px !important;
        }
    </style>
""", unsafe_allow_html=True)
