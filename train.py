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


st.write("### Numbers shown so far:")
st.write(", ".join(str(num) for num in st.session_state.output))

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
        box_num = input_positions.get((row, col))
        if box_num:
            cols[col].text_input(
                label="",
                key=f"box_{box_num}",
                value="",  # no default value
                label_visibility="collapsed",
            )
        else:
            cols[col].markdown(" ")  # empty cell placeholder

# CSS for uniform 100x100 pixel boxes
st.markdown("""
    <style>
        div[data-testid="stTextInput"] input {
            width: 50px !important;
            height: 50px !important;
            font-size: 25px !important;
            text-align: center !important;
            padding: 0 !important;
            margin: 0 auto !important;
            box-sizing: border-box !important;
        }
        div[data-testid="stTextInput"] {
            max-width: 50px !important;
            min-width: 50px !important;
             max-height: 50px !important;
            min-height: 50px !important;
            margin: 0 auto !important;
        }
    </style>
""", unsafe_allow_html=True)

st.divider()
st.subheader("Enter Your Numbers")

# Store current drawn number for input
if "current_number" not in st.session_state:
    st.session_state.current_number = None

# Update current_number when Next Number is pressed and a number is drawn
if st.button("Next Number"):
    if st.session_state.remaining_sample:
        next_num = st.session_state.remaining_sample.pop(0)
        st.session_state.output.append(next_num)
        st.session_state.current_number = next_num
    else:
        st.warning("✅ All 20 numbers shown. Click 'Reset' to start again.")
        st.session_state.current_number = None

# Mapping box positions in grid
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
        box_num = input_positions.get((row, col))
        if box_num:
            disabled = st.session_state.get(f"box_{box_num}", "") != ""
            
            # If box is empty and user clicks it, fill it with current_number (if exists)
            clicked = cols[col].button(f"Box {box_num}", key=f"btn_{box_num}", use_container_width=True)
            if clicked and not disabled and st.session_state.current_number is not None:
                st.session_state[f"box_{box_num}"] = str(st.session_state.current_number)
                # Clear current_number so it can’t be used again until next draw
                st.session_state.current_number = None
            
            cols[col].text_input(
                "",
                key=f"box_{box_num}",
                disabled=disabled,
                label_visibility="collapsed",
                placeholder="",
            )
        else:
            cols[col].markdown(" ")

# CSS for uniform 100x100 pixel boxes
st.markdown("""
    <style>
        div[data-testid="stTextInput"] input {
            width: 100px !important;
            height: 100px !important;
            font-size: 22px !important;
            text-align: center !important;
            padding: 0 !important;
            margin: 0 auto !important;
            box-sizing: border-box !important;
        }
        div[data-testid="stTextInput"] {
            max-width: 100px !important;
            min-width: 100px !important;
            margin: 0 auto !important;
        }
        button[kind="secondary"] {
            font-size: 12px;
            padding: 2px 0;
        }
    </style>
""", unsafe_allow_html=True)

