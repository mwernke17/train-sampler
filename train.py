import streamlit as st
import random

# Initialize the pool and sample on first run
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
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
    st.success("🔄 Sampling reset!")

# Display the latest number with a train image and large font
if st.session_state.output:
    latest_number = st.session_state.output[-1]
    train_img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Steam_train_icon.svg/1024px-Steam_train_icon.svg.png"
    st.markdown(
        f"""
        <div style='text-align: center; margin-top: 20px;'>
            <img src="{train_img_url}" alt="Train" width="60" style="vertical-align: middle;" />
            <span style='font-size: 60px; color: darkblue; margin-left: 10px;'>{latest_number}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("### Numbers shown so far:")
st.write(", ".join(str(num) for num in st.session_state.output))
