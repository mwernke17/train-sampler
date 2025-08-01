import streamlit as st
import random

st.set_page_config(page_title="Train Random Sampler", layout="wide")

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
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
        st.session_state[f"checked_box_{i}"] = False
    st.session_state.current_number = None

st.title("🎲 Train Random Sampler")

def draw_next_number():
    if st.session_state.remaining_sample:
        next_num = st.session_state.remaining_sample.pop(0)
        st.session_state.output.append(next_num)
        st.session_state.current_number = next_num
    else:
        st.warning("✅ All 20 numbers shown. Click 'Reset' to start again.")
        st.session_state.current_number = None

def reset_all():
    st.session_state.sampled_values = random.sample(st.session_state.original_pool, 20)
    st.session_state.remaining_sample = st.session_state.sampled_values.copy()
    st.session_state.output = []
    for i in range(1, 21):
        st.session_state[f"box_{i}"] = ""
        st.session_state[f"checked_box_{i}"] = False
    st.session_state.current_number = None
    st.success("🔄 Sampling reset!")

if st.session_state.current_number is None:
    if st.button("Next Number"):
        draw_next_number()
else:
    st.write(f"Next number to place: **{st.session_state.current_number}**")
    st.write("Please check a box next to a cell to assign this number before drawing next.")

if st.button("Reset"):
    reset_all()

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
    cols = st.columns(12, gap="large")
    for col in range(12):
        box_num = input_positions.get((row, col))
        if box_num:
            disabled = st.session_state[f"box_{box_num}"] != ""
            cb_key = f"checked_box_{box_num}"
            # Left vertical column: checkbox left, input right
            if col == 0:
                with cols[col]:
                    left_col, right_col = st.columns([1, 3])
                    with left_col:
                        if not disabled:
                            checked = st.checkbox(
                                label="",
                                key=cb_key,
                                value=st.session_state[cb_key],
                                label_visibility="collapsed",
                            )
                            # Assign current number only once when checked turns True
                            if checked and st.session_state.current_number is not None:
                                st.session_state[f"box_{box_num}"] = str(st.session_state.current_number)
                                st.session_state.current_number = None
                        else:
                            st.checkbox("", key=cb_key, value=True, disabled=True, label_visibility="collapsed")
                    with right_col:
                        st.text_input(
                            "",
                            key=f"box_{box_num}",
                            disabled=True,
                            label_visibility="collapsed",
                        )
            # Right vertical column: input left, checkbox right
            elif col == 11:
                with cols[col]:
                    left_col, right_col = st.columns([3, 1])
                    with left_col:
                        st.text_input(
                            "",
                            key=f"box_{box_num}",
                            disabled=True,
                            label_visibility="collapsed",
                        )
                    with right_col:
                        if not disabled:
                            checked = st.checkbox(
                                label="",
                                key=cb_key,
                                value=st.session_state[cb_key],
                                label_visibility="collapsed",
                            )
                            if checked and st.session_state.current_number is not None:
                                st.session_state[f"box_{box_num}"] = str(st.session_state.current_number)
                                st.session_state.current_number = None
                        else:
                            st.checkbox("", key=cb_key, value=True, disabled=True, label_visibility="collapsed")
            # Top row and others: checkbox above text input
            else:
                with cols[col]:
                    if not disabled:
                        checked = st.checkbox(
                            label="",
                            key=cb_key,
                            value=st.session_state[cb_key],
                            label_visibility="collapsed",
                        )
                        if checked and st.session_state.current_number is not None:
                            st.session_state[f"box_{box_num}"] = str(st.session_state.current_number)
                            st.session_state.current_number = None
                    else:
                        st.checkbox("", key=cb_key, value=True, disabled=True, label_visibility="collapsed")
                    st.text_input(
                        "",
                        key=f"box_{box_num}",
                        disabled=True,
                        label_visibility="collapsed",
                    )
        else:
            cols[col].markdown(" ")

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
            margin: 0 auto 5px auto !important;
            display: block !important;
            cursor: pointer;
        }
        div[role="checkbox"] {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 4px;
        }
    </style>
""", unsafe_allow_html=True)
