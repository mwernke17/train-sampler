import streamlit as st
import random

# Initialize numbers and state on first run
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
    st.session_state.current_number = None
    st.session_state.locked_boxes = set()
    st.session_state.awaiting_input = False

st.title("🎲 Train Random Sampler")

# Function to get next number
def get_next_number():
    if st.session_state.remaining_sample:
        st.session_state.current_number = st.session_state.remaining_sample.pop(0)
        st.session_state.output.append(st.session_state.current_number)
        st.session_state.awaiting_input = True
    else:
        st.warning("✅ All 20 numbers shown. Click 'Reset' to start again.")
        st.session_state.current_number = None
        st.session_state.awaiting_input = False

# Only show Next button if not waiting for input and numbers remain
next_disabled = st.session_state.awaiting_input or len(st.session_state.remaining_sample) == 0
if st.button("Next Number", disabled=next_disabled):
    get_next_number()

if st.button("Reset"):
    st.session_state.sampled_values = random.sample(st.session_state.original_pool, 20)
    st.session_state.remaining_sample = st.session_state.sampled_values.copy()
    st.session_state.output = []
    st.session_state.current_number = None
    st.session_state.locked_boxes = set()
    st.session_state.awaiting_input = False
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
    st.rerun()

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

def make_callback(box_num):
    def callback():
        key = f"box_{box_num}"
        val = st.session_state.get(key, "")
        if st.session_state.current_number is not None:
            if val == str(st.session_state.current_number):
                st.session_state.locked_boxes.add(box_num)
                st.session_state.awaiting_input = False
                st.session_state.current_number = None
                get_next_number()
    return callback

for row in range(5):
    cols = st.columns(12)
    for col in range(12):
        box_num = input_positions.get((row, col))
        if box_num:
            key = f"box_{box_num}"
            value = st.session_state.get(key, "")
            disabled = box_num in st.session_state.locked_boxes

            cols[col].text_input(
                label="",
                key=key,
                value=value,
                disabled=disabled,
                label_visibility="collapsed",
                on_change=make_callback(box_num),
            )
        else:
            cols[col].markdown(" ")

# CSS for uniform 50x50 boxes with margin
st.markdown("""
    <style>
        div[data-testid="stTextInput"] input {
            width: 50px !important;
            height: 50px !important;
            font-size: 25px !important;
            text-align: center !important;
            padding: 0 !important;
            margin: 5px auto !important;
            box-sizing: border-box !important;
        }
        div[data-testid="stTextInput"] {
            max-width: 50px !important;
            min-width: 50px !important;
            max-height: 50px !important;
            min-height: 50px !important;
            margin: 5px auto !important;
        }
    </style>
""", unsafe_allow_html=True)

# Auto-start with first number if not initialized
if st.session_state.current_number is None and st.session_state.remaining_sample and not st.session_state.awaiting_input:
    get_next_number()
