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
    # Clear all 20 text boxes
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
    st.success("🔄 Sampling reset!")

# Show train logo and last number inline only if at least one number shown
if st.session_state.output:
    number = st.session_state.output[-1]
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 20px; margin-top: 20px;">
            <img src="https://raw.githubusercontent.com/mwernke17/train-sampler/refs/heads/main/train.JPG" width="175" />
            <div style="font-size: 80px; font-weight: bold; color: red; user-select: none;">{number}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    '<h3 style="font-size: 25pt;">Numbers shown so far:</h3>', 
    unsafe_allow_html=True
)

numbers_str = ", ".join(str(num) for num in st.session_state.output)
st.markdown(
    f'<div style="font-size:20pt;">{numbers_str}</div>',
    unsafe_allow_html=True
)
