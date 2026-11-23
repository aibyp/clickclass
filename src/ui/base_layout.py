# import streamlit as st



# def style_background_home():

#     st.markdown("""
#         <style>

#                 .stApp {
#                     background: #5865F2 !important;
#                 }

#                 .stApp div[data-testid="stColumn"]{
#                     background-color:#E0E3FF !important;
#                     padding:2.5rem !important;
#                     border-radius: 5rem !important;
#                     }
#         </style>  

#                 """
#             ,unsafe_allow_html=True)
    

# def style_background_dashboard():

#     st.markdown("""
#         <style>

#                 .stApp {
#                     background: #E0E3FF !important;
#                 }

#         </style>  

#                 """
#             ,unsafe_allow_html=True)
    

    

# def style_base_layout():
# # asdasd
#     st.markdown("""
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
# #jjdskhfkdjk
                
#          /* Hide Top Bar of streamlit */
                
#             # #MainMenu, footer, header {
#             #     visibility: hidden;
#             # }
                
#             # .block-container {
#             #     padding-top:1.5rem !important;    
#             # }

#             h1 {
#                 font-family: 'Climate Crisis', sans-serif !important;
#                 font-size: 3.5rem !important;
#                 line-height:1.1 1important;
#                 margin-bottom:0rem !important;
#             }
                

#             h2 {
#                 font-family: 'Climate Crisis', sans-serif !important;
#                 font-size: 2rem !important;
#                 line-height:0.9 !important;
#                 margin-bottom:0rem !important;
#             }
                
#             h3, h4, p {
#                 font-family: 'Outfit', sans-serif;    
#             }
                

#             button{
#                 border-radius: 1.5rem !important;
#                 background-color: #5865F2 !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button[kind="secondary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: #EB459E !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button[kind="tertiary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: black !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button:hover{
#                 transform :scale(1.05)}
#         </style>  

#                 """
#             ,unsafe_allow_html=True)








########### NEW UI ####################



# import streamlit as st


# def style_background_home():

#     st.markdown("""
#         <style>

#         /* ---------- HOME: brand stage ---------- */
#         .stApp {
#             background-color: #5865F2 !important;
#             background-image:
#                 radial-gradient(60rem 40rem at 85% -10%, rgba(235, 69, 158, 0.28), transparent 60%),
#                 radial-gradient(50rem 36rem at -10% 110%, rgba(20, 22, 58, 0.35), transparent 60%) !important;
#             background-attachment: fixed !important;
#         }

#         /* Text sitting directly on the blurple stage */
#         .stApp h1,
#         .stApp h2 {
#             color: #FFFFFF !important;
#         }
#         .stApp .stMarkdown p,
#         .stApp [data-testid="stCaptionContainer"] {
#             color: rgba(255, 255, 255, 0.86) !important;
#         }

#         /* Portal cards */
#         .stApp div[data-testid="stColumn"] {
#             background: #F5F6FF !important;
#             padding: 2.5rem 2.25rem !important;
#             border-radius: 1.75rem !important;
#             border: 1px solid rgba(255, 255, 255, 0.7) !important;
#             box-shadow: 0 30px 60px -28px rgba(12, 14, 50, 0.55) !important;
#             transition: transform 0.3s ease, box-shadow 0.3s ease !important;
#         }
#         .stApp div[data-testid="stColumn"]:hover {
#             transform: translateY(-4px) !important;
#             box-shadow: 0 40px 70px -26px rgba(12, 14, 50, 0.6) !important;
#         }

#         /* Text inside the cards goes back to ink */
#         .stApp div[data-testid="stColumn"] h1,
#         .stApp div[data-testid="stColumn"] h2,
#         .stApp div[data-testid="stColumn"] h3 {
#             color: #14163A !important;
#         }
#         .stApp div[data-testid="stColumn"] .stMarkdown p,
#         .stApp div[data-testid="stColumn"] label,
#         .stApp div[data-testid="stColumn"] [data-testid="stCaptionContainer"] {
#             color: #4A4E7A !important;
#         }

#         </style>
#         """, unsafe_allow_html=True)


# def style_background_dashboard():

#     st.markdown("""
#         <style>

#         /* ---------- DASHBOARD: calm canvas ---------- */
#         .stApp {
#             background: #E0E3FF !important;
#         }

#         /* Sidebar */
#         section[data-testid="stSidebar"] {
#             background: #F5F6FF !important;
#             border-right: 1px solid #CFD3F5 !important;
#         }
#         section[data-testid="stSidebar"] > div {
#             padding-top: 1rem !important;
#         }

#         /* Metric cards */
#         div[data-testid="stMetric"] {
#             background: #FFFFFF !important;
#             border: 1px solid #D3D7F7 !important;
#             border-radius: 1.1rem !important;
#             padding: 1.1rem 1.3rem !important;
#             box-shadow: 0 10px 24px -18px rgba(20, 22, 58, 0.35) !important;
#         }
#         div[data-testid="stMetricLabel"] p {
#             color: #5B5F8A !important;
#             font-weight: 500 !important;
#             letter-spacing: 0.02em !important;
#         }
#         div[data-testid="stMetricValue"] {
#             color: #14163A !important;
#             font-weight: 700 !important;
#         }

#         /* Bordered containers (st.container(border=True)) */
#         div[data-testid="stVerticalBlockBorderWrapper"] {
#             background: #FFFFFF !important;
#             border: 1px solid #D3D7F7 !important;
#             border-radius: 1.1rem !important;
#             box-shadow: 0 10px 24px -20px rgba(20, 22, 58, 0.35) !important;
#         }

#         /* Expanders */
#         details[data-testid="stExpander"] {
#             background: #FFFFFF !important;
#             border: 1px solid #D3D7F7 !important;
#             border-radius: 1rem !important;
#         }

#         /* Tables / dataframes */
#         div[data-testid="stDataFrame"],
#         div[data-testid="stTable"] {
#             background: #FFFFFF !important;
#             border: 1px solid #D3D7F7 !important;
#             border-radius: 1rem !important;
#             overflow: hidden !important;
#             box-shadow: 0 10px 24px -20px rgba(20, 22, 58, 0.35) !important;
#         }

#         /* Tabs */
#         div[data-baseweb="tab-list"] {
#             gap: 0.5rem !important;
#             border-bottom: 1px solid #CFD3F5 !important;
#         }
#         button[data-baseweb="tab"] {
#             background: transparent !important;
#             color: #5B5F8A !important;
#             border-radius: 0.75rem 0.75rem 0 0 !important;
#             padding: 0.6rem 1.1rem !important;
#             font-weight: 500 !important;
#         }
#         button[data-baseweb="tab"][aria-selected="true"] {
#             color: #5865F2 !important;
#             font-weight: 700 !important;
#         }
#         div[data-baseweb="tab-highlight"] {
#             background-color: #5865F2 !important;
#             height: 3px !important;
#         }

#         /* Alerts: success / info / warning / error */
#         div[data-testid="stAlert"] {
#             border-radius: 1rem !important;
#             border: 1px solid #D3D7F7 !important;
#             box-shadow: 0 8px 20px -16px rgba(20, 22, 58, 0.35) !important;
#         }

#         /* Upload + camera areas */
#         section[data-testid="stFileUploaderDropzone"] {
#             background: #FFFFFF !important;
#             border: 2px dashed #A9B0F5 !important;
#             border-radius: 1.1rem !important;
#             transition: border-color 0.2s ease, background 0.2s ease !important;
#         }
#         section[data-testid="stFileUploaderDropzone"]:hover {
#             border-color: #5865F2 !important;
#             background: #F5F6FF !important;
#         }
#         div[data-testid="stCameraInput"] {
#             border-radius: 1.1rem !important;
#             overflow: hidden !important;
#         }

#         </style>
#         """, unsafe_allow_html=True)


# def style_base_layout():

#     st.markdown("""
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

#         /* ---------- Design tokens ---------- */
#         :root {
#             --cc-blurple: #5865F2;
#             --cc-blurple-dark: #4752C4;
#             --cc-lavender: #E0E3FF;
#             --cc-lavender-soft: #F5F6FF;
#             --cc-pink: #EB459E;
#             --cc-pink-dark: #C9327F;
#             --cc-ink: #14163A;
#             --cc-muted: #5B5F8A;
#             --cc-line: #D3D7F7;
#         }

#         /* ---------- Chrome ---------- */
#         #MainMenu, footer { visibility: hidden; }
#         header[data-testid="stHeader"] { background: transparent !important; }
#         .block-container {
#             padding-top: 2rem !important;
#             padding-bottom: 3rem !important;
#             max-width: 1180px !important;
#         }

#         /* ---------- Typography ---------- */
#         .stApp, .stMarkdown, p, li, label, input, textarea, button,
#         div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] {
#             font-family: 'Outfit', sans-serif;
#         }

#         h1 {
#             font-family: 'Climate Crisis', sans-serif !important;
#             font-size: 3.5rem !important;
#             line-height: 1.1 !important;
#             margin-bottom: 0 !important;
#             color: var(--cc-ink);
#         }

#         h2 {
#             font-family: 'Outfit', sans-serif !important;
#             font-weight: 700 !important;
#             font-size: 1.9rem !important;
#             line-height: 1.15 !important;
#             letter-spacing: -0.01em !important;
#             margin-bottom: 0 !important;
#             color: var(--cc-ink);
#         }

#         h3, h4 {
#             font-family: 'Outfit', sans-serif !important;
#             font-weight: 600 !important;
#             color: var(--cc-ink);
#         }

#         p, li { font-size: 1.02rem; line-height: 1.55; }

#         /* ---------- Buttons ---------- */
#         /* primary = blurple, secondary = pink, tertiary = ink */
#         button[kind="primary"],
#         button[kind="secondary"],
#         button[kind="tertiary"],
#         [data-testid="stBaseButton-primary"],
#         [data-testid="stBaseButton-secondary"],
#         [data-testid="stBaseButton-tertiary"],
#         [data-testid="stFormSubmitButton"] > button,
#         .stDownloadButton > button {
#             border-radius: 1.5rem !important;
#             padding: 0.6rem 1.4rem !important;
#             border: none !important;
#             color: #FFFFFF !important;
#             font-weight: 600 !important;
#             letter-spacing: 0.01em !important;
#             box-shadow: 0 10px 22px -12px rgba(20, 22, 58, 0.55) !important;
#             transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease !important;
#         }

#         button p { color: inherit !important; }

#         button[kind="primary"],
#         [data-testid="stBaseButton-primary"],
#         [data-testid="stFormSubmitButton"] > button,
#         .stDownloadButton > button {
#             background-color: var(--cc-blurple) !important;
#         }
#         button[kind="primary"]:hover,
#         [data-testid="stBaseButton-primary"]:hover,
#         [data-testid="stFormSubmitButton"] > button:hover,
#         .stDownloadButton > button:hover {
#             background-color: var(--cc-blurple-dark) !important;
#         }

#         button[kind="secondary"],
#         [data-testid="stBaseButton-secondary"] {
#             background-color: var(--cc-pink) !important;
#         }
#         button[kind="secondary"]:hover,
#         [data-testid="stBaseButton-secondary"]:hover {
#             background-color: var(--cc-pink-dark) !important;
#         }

#         button[kind="tertiary"],
#         [data-testid="stBaseButton-tertiary"] {
#             background-color: var(--cc-ink) !important;
#         }
#         button[kind="tertiary"]:hover,
#         [data-testid="stBaseButton-tertiary"]:hover {
#             background-color: #272A63 !important;
#         }

#         button[kind="primary"]:hover,
#         button[kind="secondary"]:hover,
#         button[kind="tertiary"]:hover,
#         [data-testid="stBaseButton-primary"]:hover,
#         [data-testid="stBaseButton-secondary"]:hover,
#         [data-testid="stBaseButton-tertiary"]:hover,
#         [data-testid="stFormSubmitButton"] > button:hover,
#         .stDownloadButton > button:hover {
#             transform: translateY(-2px) !important;
#             box-shadow: 0 16px 28px -14px rgba(20, 22, 58, 0.6) !important;
#         }

#         button:active { transform: translateY(0) scale(0.99) !important; }

#         button:focus-visible {
#             outline: 3px solid rgba(88, 101, 242, 0.45) !important;
#             outline-offset: 2px !important;
#         }

#         button:disabled {
#             opacity: 0.5 !important;
#             cursor: not-allowed !important;
#             transform: none !important;
#             box-shadow: none !important;
#         }

#         /* ---------- Form inputs ---------- */
#         div[data-baseweb="input"],
#         div[data-baseweb="textarea"],
#         div[data-baseweb="select"] > div {
#             background: #FFFFFF !important;
#             border: 1px solid var(--cc-line) !important;
#             border-radius: 0.9rem !important;
#             transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
#         }
#         div[data-baseweb="input"]:focus-within,
#         div[data-baseweb="textarea"]:focus-within,
#         div[data-baseweb="select"] > div:focus-within {
#             border-color: var(--cc-blurple) !important;
#             box-shadow: 0 0 0 3px rgba(88, 101, 242, 0.2) !important;
#         }
#         div[data-baseweb="input"] input,
#         div[data-baseweb="textarea"] textarea {
#             color: var(--cc-ink) !important;
#             background: transparent !important;
#         }
#         label[data-testid="stWidgetLabel"] p {
#             color: var(--cc-muted) !important;
#             font-weight: 500 !important;
#             font-size: 0.92rem !important;
#         }

#         /* ---------- Misc ---------- */
#         hr { border-color: var(--cc-line) !important; }
#         </style>
#         """, unsafe_allow_html=True)





####333NEW 2##############333



import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

        /* ================= HOME ================= */
        .stApp {
            background-color: #0F1133 !important;
            background-image:
                radial-gradient(rgba(255,255,255,0.07) 1.2px, transparent 1.2px),
                radial-gradient(55rem 35rem at 92% -8%, rgba(88,101,242,0.60), transparent 62%),
                radial-gradient(40rem 30rem at -5% 105%, rgba(235,69,158,0.28), transparent 62%) !important;
            background-size: 28px 28px, auto, auto !important;
            background-attachment: fixed !important;
        }

        .stApp::after {
            content: "AI-POWERED ATTENDANCE  ·  FACE RECOGNITION  ·  ZERO ROLL CALLS";
            position: fixed;
            bottom: 1rem;
            left: 0; right: 0;
            text-align: center;
            font-family: 'Outfit', sans-serif;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.28em;
            color: rgba(255,255,255,0.42);
            pointer-events: none;
            z-index: 1;
        }

        .stApp h1 {
            color: #FFFFFF !important;
            font-size: 4.2rem !important;
            text-shadow: 5px 5px 0 #EB459E;
            padding-bottom: 0.6rem !important;
        }
        .stApp h2 { color: #FFFFFF !important; }
        .stApp .stMarkdown p,
        .stApp [data-testid="stCaptionContainer"] {
            color: rgba(255,255,255,0.80) !important;
            font-size: 1.1rem !important;
        }

        div[data-testid="stHorizontalBlock"] {
            gap: 2.75rem !important;
            margin-top: 2.5rem !important;
        }

        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
            position: relative !important;
            background: #F7F8FF !important;
            border: 2px solid #0F1133 !important;
            border-radius: 1.25rem !important;
            padding: 3rem 2.25rem 2.25rem 2.25rem !important;
            box-shadow: 8px 8px 0 #5865F2 !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:hover {
            transform: translate(-3px, -3px) !important;
            box-shadow: 11px 11px 0 #5865F2 !important;
        }

        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]::before {
            position: absolute;
            top: -1.05rem;
            left: 1.5rem;
            padding: 0.4rem 0.95rem;
            border: 2px solid #0F1133;
            border-radius: 999px;
            color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            z-index: 2;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]::after {
            position: absolute;
            top: 1.1rem;
            right: 1.5rem;
            font-size: 2rem;
            opacity: 0.9;
        }

        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child(1)::before {
            content: "01 · TEACHER PORTAL";
            background: #5865F2;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child(1)::after {
            content: "🧑‍🏫";
        }

        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child(2) {
            box-shadow: 8px 8px 0 #EB459E !important;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child(2):hover {
            box-shadow: 11px 11px 0 #EB459E !important;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child(2)::before {
            content: "02 · STUDENT PORTAL";
            background: #EB459E;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child(2)::after {
            content: "🎒";
        }

        div[data-testid="stColumn"] h1,
        div[data-testid="stColumn"] h2,
        div[data-testid="stColumn"] h3 {
            color: #0F1133 !important;
            text-shadow: none !important;
            font-size: 2.1rem !important;
        }
        div[data-testid="stColumn"] .stMarkdown p,
        div[data-testid="stColumn"] label p,
        div[data-testid="stColumn"] [data-testid="stCaptionContainer"] {
            color: #4A4E7A !important;
            font-size: 1.02rem !important;
        }

        div[data-testid="stColumn"] button {
            width: 100% !important;
            padding: 0.85rem 1.4rem !important;
        }
        div[data-testid="stColumn"] button p::after {
            content: "  →";
        }

        div[data-testid="stColumn"] div[data-testid="stHorizontalBlock"] {
            margin-top: 0 !important;
            gap: 1rem !important;
        }
        div[data-testid="stColumn"] div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"],
        div[data-testid="stColumn"] div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:hover {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            border-radius: 0 !important;
            transform: none !important;
        }
        div[data-testid="stColumn"] div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]::before,
        div[data-testid="stColumn"] div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]::after {
            content: none !important;
        }

        </style>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------------
# Dashboards: same dark stage as home, content on a paper panel.
# Teacher = blurple accent, Student = pink accent.
# ---------------------------------------------------------------
_DASHBOARD_CSS = """
<style>

/* ---------- Stage ---------- */
.stApp {
    background-color: #0F1133 !important;
    background-image:
        radial-gradient(rgba(255,255,255,0.07) 1.2px, transparent 1.2px),
        radial-gradient(55rem 35rem at 92% -8%, __GLOW__, transparent 62%),
        radial-gradient(40rem 30rem at -5% 105%, __GLOW2__, transparent 62%) !important;
    background-size: 28px 28px, auto, auto !important;
    background-attachment: fixed !important;
}

/* ---------- Main paper panel ---------- */
.stApp .block-container {
    position: relative !important;
    background: #F7F8FF !important;
    border: 2px solid #0F1133 !important;
    border-radius: 1.5rem !important;
    box-shadow: 10px 10px 0 __ACCENT__ !important;
    margin: 3rem auto 4rem auto !important;
    padding: 3.2rem 2.6rem 2.6rem 2.6rem !important;
    max-width: 1120px !important;
}
.stApp .block-container::before {
    content: "__LABEL__";
    position: absolute;
    top: -1.05rem;
    left: 2rem;
    padding: 0.4rem 1rem;
    border: 2px solid #0F1133;
    border-radius: 999px;
    background: __ACCENT__;
    color: #FFFFFF;
    font-family: 'Outfit', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.16em;
}

/* Headings */
.stApp h1 {
    color: #0F1133 !important;
    font-size: 2.6rem !important;
    text-shadow: none !important;
    padding-bottom: 1rem !important;
}
.stApp h1::after {
    content: "";
    display: block;
    width: 4rem;
    height: 6px;
    margin-top: 0.8rem;
    background: __ACCENT2__;
    border-radius: 99px;
}
.stApp h2 { color: #0F1133 !important; margin-top: 1.2rem !important; }
.stApp h3, .stApp h4 { color: #0F1133 !important; }
.stApp .stMarkdown p,
.stApp [data-testid="stCaptionContainer"] { color: #3B3F6B; }

/* Nested columns stay plain */
div[data-testid="stHorizontalBlock"] { gap: 1.25rem !important; }

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background: #0A0C26 !important;
    border-right: 2px solid __ACCENT__ !important;
}
section[data-testid="stSidebar"] > div { padding-top: 1.5rem !important; }
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span { color: #E8EAFF !important; }
section[data-testid="stSidebar"] h1 {
    font-size: 1.6rem !important;
    padding-bottom: 0.4rem !important;
}
section[data-testid="stSidebar"] h1::after {
    background: __ACCENT__; height: 4px; width: 2.5rem;
}
section[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.15) !important; }

section[data-testid="stSidebar"] button[kind],
section[data-testid="stSidebar"] [data-testid^="stBaseButton"] {
    width: 100% !important;
    justify-content: flex-start !important;
    text-align: left !important;
    background: rgba(255,255,255,0.07) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255,255,255,0.16) !important;
    box-shadow: none !important;
    border-radius: 0.8rem !important;
}
section[data-testid="stSidebar"] button[kind]:hover,
section[data-testid="stSidebar"] [data-testid^="stBaseButton"]:hover {
    background: #B8FF3C !important;
    color: #0F1133 !important;
    transform: translateX(3px) !important;
    box-shadow: none !important;
}

/* ---------- Metric cards ---------- */
div[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 2px solid #0F1133 !important;
    border-left: 8px solid __ACCENT__ !important;
    border-radius: 1rem !important;
    padding: 1.2rem 1.4rem !important;
    box-shadow: 5px 5px 0 #0F1133 !important;
}
div[data-testid="stMetricLabel"] p {
    color: #5B5F8A !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
}
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] * {
    font-family: 'Climate Crisis', sans-serif !important;
    font-size: 2.3rem !important;
    color: #0F1133 !important;
}

/* ---------- Containers / expanders / tables ---------- */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF !important;
    border: 2px solid #0F1133 !important;
    border-radius: 1rem !important;
    box-shadow: 5px 5px 0 __ACCENT_SOFT__ !important;
}
details[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 2px solid #0F1133 !important;
    border-radius: 1rem !important;
}
div[data-testid="stDataFrame"],
div[data-testid="stTable"] {
    background: #FFFFFF !important;
    border: 2px solid #0F1133 !important;
    border-radius: 1rem !important;
    overflow: hidden !important;
    box-shadow: 5px 5px 0 __ACCENT_SOFT__ !important;
}

/* ---------- Tabs ---------- */
div[data-baseweb="tab-list"] {
    gap: 0.6rem !important;
    border-bottom: none !important;
    padding-bottom: 0.6rem !important;
}
button[data-baseweb="tab"] {
    background: #FFFFFF !important;
    color: #0F1133 !important;
    border: 2px solid #0F1133 !important;
    border-radius: 999px !important;
    padding: 0.45rem 1.2rem !important;
    font-weight: 600 !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    background: __ACCENT__ !important;
    color: #FFFFFF !important;
}
button[data-baseweb="tab"][aria-selected="true"] p { color: #FFFFFF !important; }
div[data-baseweb="tab-highlight"],
div[data-baseweb="tab-border"] { display: none !important; }

/* ---------- Alerts ---------- */
div[data-testid="stAlert"] {
    border: 2px solid #0F1133 !important;
    border-radius: 1rem !important;
    box-shadow: 4px 4px 0 #0F1133 !important;
}

/* ---------- Upload + camera ---------- */
section[data-testid="stFileUploaderDropzone"] {
    background: #FFFFFF !important;
    border: 2px dashed __ACCENT__ !important;
    border-radius: 1.1rem !important;
    padding: 1.6rem !important;
    transition: background 0.2s ease !important;
}
section[data-testid="stFileUploaderDropzone"]:hover { background: #EEF0FF !important; }
div[data-testid="stCameraInput"] {
    border: 2px solid #0F1133 !important;
    border-radius: 1.1rem !important;
    overflow: hidden !important;
    box-shadow: 5px 5px 0 __ACCENT_SOFT__ !important;
}

</style>
"""


def _render_dashboard(label, accent, accent2, accent_soft, glow, glow2):
    css = (_DASHBOARD_CSS
           .replace("__LABEL__", label)
           .replace("__ACCENT2__", accent2)
           .replace("__ACCENT_SOFT__", accent_soft)
           .replace("__ACCENT__", accent)
           .replace("__GLOW2__", glow2)
           .replace("__GLOW__", glow))
    st.markdown(css, unsafe_allow_html=True)


def style_background_dashboard(role="teacher"):
    if role == "student":
        _render_dashboard(
            "STUDENT PORTAL", "#EB459E", "#5865F2", "rgba(235,69,158,0.40)",
            "rgba(235,69,158,0.50)", "rgba(88,101,242,0.30)")
    else:
        _render_dashboard(
            "TEACHER PORTAL", "#5865F2", "#EB459E", "rgba(88,101,242,0.40)",
            "rgba(88,101,242,0.60)", "rgba(235,69,158,0.22)")


def style_background_teacher():
    style_background_dashboard("teacher")


def style_background_student():
    style_background_dashboard("student")


def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        :root {
            --cc-blurple: #5865F2;
            --cc-pink: #EB459E;
            --cc-ink: #0F1133;
            --cc-lime: #B8FF3C;
            --cc-cyan: #22D3EE;
            --cc-muted: #5B5F8A;
        }

        /* ---------- Chrome ---------- */
        #MainMenu, footer,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"] { display: none !important; }
        header[data-testid="stHeader"] { background: transparent !important; }
        .block-container {
            padding-top: 2.5rem !important;
            padding-bottom: 4rem !important;
            max-width: 1120px !important;
        }

        /* ---------- Typography ---------- */
        .stApp, .stMarkdown, p, li, label, input, textarea, button {
            font-family: 'Outfit', sans-serif;
        }
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0 !important;
        }
        h2 {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 800 !important;
            font-size: 1.9rem !important;
            line-height: 1.15 !important;
            letter-spacing: -0.015em !important;
            margin-bottom: 0 !important;
        }
        h3, h4 {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 700 !important;
        }
        p, li { font-size: 1.02rem; line-height: 1.55; }

        /* ---------- Buttons: lime / cyan / ink ---------- */
        button[kind="primary"],
        button[kind="secondary"],
        button[kind="tertiary"],
        [data-testid="stBaseButton-primary"],
        [data-testid="stBaseButton-secondary"],
        [data-testid="stBaseButton-tertiary"],
        [data-testid="stFormSubmitButton"] > button,
        .stDownloadButton > button {
            border: 2px solid var(--cc-ink) !important;
            border-radius: 0.9rem !important;
            padding: 0.65rem 1.5rem !important;
            font-weight: 800 !important;
            letter-spacing: 0.02em !important;
            box-shadow: 3px 3px 0 var(--cc-ink) !important;
            transition: transform 0.15s ease, box-shadow 0.15s ease, filter 0.15s ease !important;
        }
        button p { color: inherit !important; font-weight: inherit !important; }

        /* Primary: electric lime */
        button[kind="primary"],
        [data-testid="stBaseButton-primary"],
        [data-testid="stFormSubmitButton"] > button,
        .stDownloadButton > button {
            background-color: var(--cc-lime) !important;
            color: var(--cc-ink) !important;
        }
        /* Secondary: cyan */
        button[kind="secondary"],
        [data-testid="stBaseButton-secondary"] {
            background-color: var(--cc-cyan) !important;
            color: var(--cc-ink) !important;
        }
        /* Tertiary: ink with lime */
        button[kind="tertiary"],
        [data-testid="stBaseButton-tertiary"] {
            background-color: var(--cc-ink) !important;
            color: var(--cc-lime) !important;
            border-color: var(--cc-lime) !important;
            box-shadow: 3px 3px 0 var(--cc-lime) !important;
        }

        button[kind="primary"]:hover,
        button[kind="secondary"]:hover,
        [data-testid="stBaseButton-primary"]:hover,
        [data-testid="stBaseButton-secondary"]:hover,
        [data-testid="stFormSubmitButton"] > button:hover,
        .stDownloadButton > button:hover {
            transform: translate(-2px, -2px) !important;
            box-shadow: 5px 5px 0 var(--cc-ink) !important;
            filter: brightness(1.05);
        }
        button[kind="tertiary"]:hover,
        [data-testid="stBaseButton-tertiary"]:hover {
            transform: translate(-2px, -2px) !important;
            box-shadow: 5px 5px 0 var(--cc-lime) !important;
        }
        button:active {
            transform: translate(2px, 2px) !important;
            box-shadow: 0 0 0 var(--cc-ink) !important;
        }
        button:focus-visible {
            outline: 3px solid rgba(34,211,238,0.7) !important;
            outline-offset: 3px !important;
        }
        button:disabled {
            opacity: 0.45 !important;
            cursor: not-allowed !important;
            transform: none !important;
            box-shadow: none !important;
        }

        /* ---------- Inputs ---------- */
        div[data-baseweb="input"],
        div[data-baseweb="textarea"],
        div[data-baseweb="select"] > div {
            background: #FFFFFF !important;
            border: 2px solid var(--cc-ink) !important;
            border-radius: 0.8rem !important;
            transition: box-shadow 0.15s ease, transform 0.15s ease !important;
        }
        div[data-baseweb="input"]:focus-within,
        div[data-baseweb="textarea"]:focus-within,
        div[data-baseweb="select"] > div:focus-within {
            box-shadow: 3px 3px 0 var(--cc-blurple) !important;
            transform: translate(-1px, -1px);
        }
        div[data-baseweb="input"] input,
        div[data-baseweb="textarea"] textarea {
            color: var(--cc-ink) !important;
            background: transparent !important;
        }
        label[data-testid="stWidgetLabel"] p {
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            letter-spacing: 0.02em !important;
        }

        hr { border-color: rgba(15,17,51,0.2) !important; }
        </style>
        """, unsafe_allow_html=True)










