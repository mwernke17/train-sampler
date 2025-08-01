import streamlit as st
import random

if 'original_pool' not in st.session_state:
    st.session_state.original_pool = [
        1,2,3,4,5,6,7,8,9,10,
        11,11,12,12,13,13,14,14,15,15,
        16,16,17,17,18,18,19,19,
        20,21,22,23,24,25,26,27,28,29,30
    ]
    st.session_state.sampled_values = random.sample(st.session_state.original_pool, 20)
    st.session_state.remaining_sample = st.session_state.sampled_values.copy()
    st.session_state.output = []

st.title("🎲 Train Random Sampler")

# Train logo near the top
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Steam_locomotive_icon.svg",
    width=120,
    output_format="PNG"
)

if st.button("Next Number"):
    if st.session_state.remaining_sample:
        next_number = st.session_state.remaining_sample.pop(0)
        st.session_state.output.append(next_number)
    else:
        st.warning("✅ All 20 numbers shown. Click 'Reset' to start again.")

if st.button("Reset"):
    st.session_state.sampled_values = random.sample(st.session_state.original_pool, 20)
    st.session_state.remaining_sample = st.session_state.sampled_values.copy()
    st.session_state.output = []
    st.success("🔄 Sampling reset!")

st.write("### Numbers shown so far:")
st.write(", ".join(str(num) for num in st.session_state.output))

st.divider()
st.subheader("Enter Your Numbers")

# Define inputs layout with columns and uniform size boxes
left_col, center_col, right_col = st.columns([1, 3, 1])

with left_col:
    # boxes 1 to 5 (bottom to top)
    for i in reversed(range(5)):
        st.text_input("", key=f"box_{i+1}", label_visibility="collapsed", max_chars=2, placeholder="", help=f"Box {i+1}")

with center_col:
    # boxes 6 to 15 across the top
    top_cols = st.columns(10)
    for i in range(10):
        top_cols[i].text_input("", key=f"box_{i+6}", label_visibility="collapsed", max_chars=2, placeholder="", help=f"Box {i+6}")

with right_col:
    # boxes 16 to 20 (top to bottom)
    for i in range(5):
        st.text_input("", key=f"box_{i+16}", label_visibility="collapsed", max_chars=2, placeholder="", help=f"Box {i+16}")

# CSS for uniform input box size and style
st.markdown("""
    <style>
        div[data-testid="stTextInput"] input {
            width: 100px !important;
            height: 50px !important;
            font-size: 20px !important;
            text-align: center !important;
        }
    </style>
""", unsafe_allow_html=True)
