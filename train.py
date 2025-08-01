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

left_col, center_col, right_col = st.columns([1, 10, 1])

# Left column: boxes 1 to 5, bottom to top (reverse order in code)
with left_col:
    for i in reversed(range(1, 6)):
        st.text_input(
            label="",
            key=f"box_{i}",
            placeholder="",
            label_visibility="collapsed",
        )

# Center column: boxes 6 to 15, left to right
with center_col:
    top_cols = st.columns(10)
    for i in range(6, 16):
        top_cols[i - 6].text_input(
            label="",
            key=f"box_{i}",
            placeholder="",
            label_visibility="collapsed",
        )

# Right column: boxes 16 to 20, top to bottom
with right_col:
    for i in range(16, 21):
        st.text_input(
            label="",
            key=f"box_{i}",
            placeholder="",
            label_visibility="collapsed",
        )

# CSS for uniform 75x75 px boxes
st.markdown("""
    <style>
        div[data-testid="stTextInput"] input {
            width: 75px !important;
            height: 75px !important;
            font-size: 20px !important;
            text-align: center !important;
            padding: 0 !important;
            margin: 5px auto !important;
            box-sizing: border-box !important;
        }
        div[data-testid="stTextInput"] {
            max-width: 75px !important;
            min-width: 75px !important;
            margin: 0 auto !important;
        }
    </style
