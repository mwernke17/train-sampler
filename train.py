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

if st.session_state.output:
    cols = st.columns([1, 2])  # train image takes less width
    with cols[0]:
        st.image("https://raw.githubusercontent.com/mwernke17/train-sampler/refs/heads/main/train.JPG", width=200)
    with cols[1]:
        st.markdown(
            f"<h1 style='display: flex; align-items: center; height: 200px; margin: 0;'>"
            f"{st.session_state.output[-1]}"
            f"</h1>", 
            unsafe_allow_html=True
        )

if st.button("Reset"):
    st.session_state.sampled_values = random.sample(st.session_state.original_pool, 20)
    st.session_state.remaining_sample = st.session_state.sampled_values.copy()
    st.session_state.output = []
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
    st.success("🔄 Sampling reset!")

st.write("### Numbers shown so far:")
st.write(", ".join(str(num) for num in st.session_state.output))
