import streamlit as st
import random

# Initialize original pool and sampling
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
    # Initialize text boxes empty and checkbox states false
    for i in range(1, 21):
        st.session_state.setdefault(f"box_{i}", "")
        st.session_state.setdefault(f"checked_box_{i}", False)

st.title("🎲 Train Random Sampler")

# Disable "Next Number" button if current_number is waiting to be entered
next_disabled = st.session_state.current_number is not None

if st.button("Next Number", disabled=next_disabled):
    if st.session_state.remaining_sample:
        next_number = st.session_state.remaining_sample.pop(0)
        st.session_state.output.append(next_number)
        st.session_state.current_number = next_number
    else:
        st.warning("✅ All 20 numbers shown. Click 'Reset' to start again.")
        st.session_state.current_number = None

if st.button("Reset"):
    st.session_state.sampled_values = random.sample(st.session_state.original_pool, 20)
    st.session_state.remaining_sample = st.session_state.sampled_values.copy()
    st.session_state.output = []
    st.session_state.current_number = None
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
        st.session_state[f"checked_box_{i}"] = False
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

# Sync checked state based on filled boxes
for i in range(1, 21):
    if st.session_state.get(f"box_{i}", "") != "":
        st.session_state[f"checked_box_{i}"] = True
    else:
        # Reset checkbox if box empty and no current_number waiting
        if st.session_state.get(f"checked_box_{i}", False) and st.session_state.current_number is None:
            st.session_state[f"checked_box_{i}"] = False

for row in range(5):
    cols = st.columns(12)
    for col in range(12):
        box_num = input_positions.get((row, col))
        if box_num:
            disabled = st.session_state.get(f"box_{box_num}", "") != ""
            cb_key = f"checked_box_{box_num}"
            checked_val = st.session_state[cb_key]

            # For left vertical column (col=0): checkbox to left, textbox to right
            if col == 0 and row in range(5):
                with cols[col]:
                    left_col, right_col = st.columns([1,4])
                    with left_col:
                        checked = st.checkbox(
                            label="",
                            value=checked_val,
                            key=cb_key,
                            disabled=disabled,
                            label_visibility="collapsed",
                        )
                    with right_col:
                        st.text_input(
                            "",
                            key=f"box_{box_num}",
                            disabled=disabled,
                            label_visibility="collapsed",
                            placeholder="",
                        )
            # For right vertical column (col=11): text box to left, checkbox to right
            elif col == 11 and row in range(5):
                with cols[col]:
                    left_col, right_col = st.columns([4,1])
                    with left_col:
                        st.text_input(
                            "",
                            key=f"box_{box_num}",
                            disabled=disabled,
                            label_visibility="collapsed",
                            placeholder="",
                        )
                    with right_col:
                        checked = st.checkbox(
                            label="",
                            value=checked_val,
                            key=cb_key,
                            disabled=disabled,
                            label_visibility="collapsed",
                        )
            # Elsewhere: checkbox above text input (center top row)
            else:
                with cols[col]:
                    checked = st.checkbox(
                        label="",
                        value=checked_val,
                        key=cb_key,
                        disabled=disabled,
                        label_visibility="collapsed",
                    )
                    st.text_input(
                        "",
                        key=f"box_{box_num}",
                        disabled=disabled,
                        label_visibility="collapsed",
                        placeholder="",
                    )
            
            # Handle checkbox clicked logic
            if checked and not disabled and st.session_state.current_number is not None:
                st.session_state[f"box_{box_num}"] = str(st.session_state.current_number)
                st.session_state.current_number = None
                st.session_state[cb_key] = True
        else:
            cols[col].markdown(" ")

# CSS adjustments for spacing
st.markdown("""
    <style>
        div[data-testid="stTextInput"] {
            max-width: 75px !important;
            min-width: 75px !important;
            max-height: 75px !important;
            min-height: 75px !important;
            margin: 0 auto 10px auto !important;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        div[data-testid="stTextInput"] input {
            width: 50px !important;
            height: 50px !important;
            font-size: 22px !important;
            text-align: center !important;
            padding: 0 !important;
            margin: 0 auto !important;
            box-sizing: border-box !important;
        }
        input[type="checkbox"] {
            width: 15px !important;
            height: 15px !important;
            margin: 0 auto !important;
            display: block !important;
        }
        div[role="checkbox"] {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 4px;
        }
        /* Add 20px gap between top row columns (cols 1 to 10 in row 0) */
        /* Note: Streamlit columns don't have easy direct selectors; workaround with margin */
        section[data-testid="stColumns"] > div:nth-child(1) > div > div > div:nth-child(1) {
            margin-right: 20px !important;
        }
        /* Add margin-right to top row except last box (16th box col=11) */
        /* We add margin-right to cols in row=0 and col=1 to 10 */
        /* Unfortunately, no direct CSS selector for grid cells, so adding margin-right on all except last column */
        section[data-testid="stColumns"] > div > div > div > div > div > div > div > div {
            margin-right: 0px !important;
        }
    </style>
""", unsafe_allow_html=True)
