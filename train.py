import streamlit as st
import random

# --- Initialization ---

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
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
        st.session_state[f"chk_{i}"] = False

st.title("🎲 Train Random Sampler")

# --- Next Number Button ---
next_button_disabled = st.session_state.current_number is not None
if st.button("Next Number", disabled=next_button_disabled):
    if st.session_state.remaining_sample:
        next_num = st.session_state.remaining_sample.pop(0)
        st.session_state.output.append(next_num)
        st.session_state.current_number = next_num
    else:
        st.warning("✅ All 20 numbers shown. Click 'Reset' to start again.")
        st.session_state.current_number = None

# --- Reset Button ---
if st.button("Reset"):
    st.session_state.sampled_values = random.sample(st.session_state.original_pool, 20)
    st.session_state.remaining_sample = st.session_state.sampled_values.copy()
    st.session_state.output = []
    st.session_state.current_number = None
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
        st.session_state[f"chk_{i}"] = False
    st.success("🔄 Sampling reset!")

st.write("### Numbers shown so far:")
st.write(", ".join(str(num) for num in st.session_state.output))

st.divider()
st.subheader("Enter Your Numbers")

# --- Layout Setup ---

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

# Render the grid row by row
for row in range(5):
    cols = st.columns(12, gap="medium")
    for col in range(12):
        box_num = input_positions.get((row, col))
        if box_num:
            # Is box filled?
            disabled = st.session_state[f"box_{box_num}"] != ""

            # Left column checkboxes (col 0)
            if col == 0:
                with cols[col]:
                    checked = st.checkbox(
                        label="",
                        key=f"chk_{box_num}",
                        disabled=disabled or (st.session_state.current_number is None),
                        value=st.session_state[f"chk_{box_num}"],
                        label_visibility="collapsed",
                        help=f"Check to assign current number to box {box_num}",
                    )
                with cols[col+1]:
                    st.text_input(
                        label="",
                        key=f"box_{box_num}",
                        value=st.session_state[f"box_{box_num}"],
                        disabled=True,
                        label_visibility="collapsed",
                    )
                # If checkbox just checked, assign number
                if checked and not disabled and st.session_state.current_number is not None:
                    st.session_state[f"box_{box_num}"] = str(st.session_state.current_number)
                    st.session_state.current_number = None
                    st.session_state[f"chk_{box_num}"] = False

            # Right column checkboxes (col 11)
            elif col == 11:
                with cols[col-1]:
                    st.text_input(
                        label="",
                        key=f"box_{box_num}",
                        value=st.session_state[f"box_{box_num}"],
                        disabled=True,
                        label_visibility="collapsed",
                    )
                with cols[col]:
                    checked = st.checkbox(
                        label="",
                        key=f"chk_{box_num}",
                        disabled=disabled or (st.session_state.current_number is None),
                        value=st.session_state[f"chk_{box_num}"],
                        label_visibility="collapsed",
                        help=f"Check to assign current number to box {box_num}",
                    )
                if checked and not disabled and st.session_state.current_number is not None:
                    st.session_state[f"box_{box_num}"] = str(st.session_state.current_number)
                    st.session_state.current_number = None
                    st.session_state[f"chk_{box_num}"] = False

            # Top row text inputs only (cols 1 to 10)
            else:
                with cols[col]:
                    st.text_input(
                        label="",
                        key=f"box_{box_num}",
                        value=st.session_state[f"box_{box_num}"],
                        disabled=True,
                        label_visibility="collapsed",
                    )
        else:
            cols[col].markdown(" ")  # empty cell

# --- CSS Styling ---
st.markdown(
    """
    <style>
        /* Container size */
        .stTextInput > div {
            max-width: 75px !important;
            min-width: 75px !important;
            max-height: 75px !important;
            min-height: 75px !important;
            margin: 0 auto !important;
        }
        /* Input box size */
        div[data-testid="stTextInput"] input {
            width: 50px !important;
            height: 50px !important;
            font-size: 22px !important;
            text-align: center !important;
            padding: 0 !important;
            margin: 0 auto !important;
            box-sizing: border-box !important;
        }
        /* Checkbox size */
        input[type="checkbox"] {
            width: 20px !important;
            height: 20px !important;
            margin-top: 15px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
