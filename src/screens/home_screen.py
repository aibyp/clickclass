import streamlit as st
from src.components.header  import header_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():

    header_home()
    style_background_home()
    style_base_layout()
    col1,col2= st.columns(2,gap="large")

    with col1:
        st.header("I am Teacher")
        st.image("https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.0/assets/svg/1f9d1-200d-1f3eb.svg", width=145)
        if st.button("Teacher portal"):
            st.session_state['login_type']='teacher'
            st.rerun
    with col2:
        st.header("I am Student")
        st.image("	https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.0/assets/svg/1f9d1-200d-1f393.svg", width=120)
        if st.button("Student portal"):
            st.session_state['login_type']='student'
            st.rerun