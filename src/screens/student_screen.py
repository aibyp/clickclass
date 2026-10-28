import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendence,get_face_embeddings,train_classifier
from src.database.db import get_all_students,create_student
from PIL import Image
import numpy as np


def student_dashboard():
     st.header("Student dashboard!!!!!")
def student_screen():

    style_background_dashboard()

    style_base_layout()

    if "student_data" in st.session_state:
         student_dashboard()
         return 
    
    c1,c2=st.columns(2, vertical_alignment='center', gap='xxlarge') 
    with c1:
            header_dashboard
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type']=None
            st.rerun()  #when ever state changes we need to rerun it .
    header_dashboard()

    st.header("Login using faceID")
    st.space() 
    st.space()

    show_registration=False  # to know the state of studnet login/new studnet that needs to register
    photo_source=st.camera_input("Position ur face in center")
    if photo_source:
         img=np.array(Image.open(photo_source))

         with st.spinner("AI Is Scanning"):   #while ai is doing its job of predicting , it spins
            detected, all_ids,num_faces= predict_attendence(img)

            if num_faces==0:
                st.warning("No face found!!!")
            elif num_faces>1:
             st.warning("Multiple faces found!!!")
            else:
                if detected:
                    student_id=list(detected.keys())[0]
                    all_students=get_all_students()
                    student=next((s for s in all_students if s['student_id']==student_id),None)


                    if student:
                        st.session_state.is_logged_in=True
                        st.session_state.user_role='student'
                        st.session_state.student_data=student
                        st.toast("Welcome back  Verto ")
                        import time
                        time.sleep(1)
                        st.rerun()
                else:
                  st.info("Face not recognized , You might be a New Verto")
                  show_registration=True
    if show_registration:
         with st.container(border=True):
              st.header("Register new Profile")
              new_name=st.text_input("Enter ur name", placeholder="E.g:Sanskriti")
              if st.button("Create Account", type="primary"):
                   if new_name:
                        with st.spinner("Creating ur profile"): #its going to spin till all data base works are done
                             img=np.array(Image.open(photo_source))
                             encodings=get_face_embeddings(img)
                             if encodings:
                                  face_emb=encodings[0].tolist()
                             response_data=create_student(new_name,face_embedding=face_emb)

                             if response_data:  # we got resposne so we need to refit data! , train
                                  #again as the new entry is added to the database
                                  train_classifier()
                                  st.session_state.is_logged_in=True
                                  st.session_state.user_role='student'
                                  st.session_state.student_data=response_data[0]
                                  st.toast("Profile Created Verto")
                                  import time
                                  time.sleep(1)
                                  st.rerun
                             else:
                                  st.error("Couldnt capture face for recognization")
                   else:
                        st.warning("Please enter ur name")

    footer_dashboard()