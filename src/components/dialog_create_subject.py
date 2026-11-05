import streamlit as st
from src.database.db import create_subject


# dialogs ar ecreated like this in streamlit 
@st.dialog("Create new subject")    
def create_subject_dialog(teacher_id):
    st.write("Enter the details of ur subject")
    sub_id =st.text_input("Course Code",placeholder="INT395")
    sub_name=st.text_input("Course Name",placeholder="Supervised Learning")
    sub_section=st.text_input("Section Name",placeholder="K24WV")

    if st.button("Create Subject Now", type="primary",width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Course Created Successfully")
                st.rerun()
            except Exception as e:
                st.error("Error: {str(e)}")
        else:
            st.warning("Please enter all fields")
