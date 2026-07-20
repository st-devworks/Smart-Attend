import streamlit as st
import config


def login():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.title("🎓 SmartAttend")
    st.subheader("Administrator Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        if (
            username.strip() == config.ADMIN_USERNAME.strip()
            and
            password.strip() == config.ADMIN_PASSWORD.strip()
        ):

            st.session_state.logged_in = True
            st.rerun()

        else:

            st.error("Invalid Username or Password")

    return False