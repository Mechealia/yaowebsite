import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Qiyao Introduction",
    page_icon="👋",
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


with st.container():
    left, right = st.columns((2, 3), gap='small')
    with right:
        st.title("I Am Here")
        st.sidebar.success("Select a page above")
        st.subheader("Hello, Welcome to My Page 👋")
        st.write("📍Bordeaux, France")
        st.write("Hi, my name is Qiyao HE. Welcome! Welcome! Welcome! I built this webpage with self-learning knowledge so it looks not pretty and professional enough, please understand me. Super welcome to my page, if you want to know more about me, please explore on this page.")
    with left:
        image = Image.open('meweb.png')
        st.image(image, width=230)


st.write('---')
st.header('Contact Me')
c1, c2 = st.columns(2)
with st.container():
    c1.write("Linkedin: https://www.linkedin.com/in/qiyao-he")
    c2.write("Email: mechealia.he3378@outlook.com")


with st.container():
    st.write("---")

    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who Is Qiyao HE:")
        st.write("##")
        st.write(
            """
            I am Qiyao , master of supply chain management graduated from KEDGE business school in the year 2020, since then I have been working in different roles and industries for several years. I enjoy learning and love to use what i learned into the job.
            - I speak Chinese 🇨🇳, English 🇬🇧 and French 🇨🇵
            - I am experienced Project Coordinator, cross-functional communicator and customer facing problem solver. Worked in data-oriented environment and a passion for delivering high quality customer oriented projects. 
            - I worked as a cyber security coordinator, software analyst and customer agent
            - Now I am looking for a new job opportunity
            
            
            """
        )
    with right_column:
        import streamlit as st
        import json
        import streamlit.components.v1 as com
        from streamlit_lottie import st_lottie
        with open("woman1.json") as source:
            woman1 = json.load(source)
        st_lottie(woman1)


st.write('---')
st.header('My Interests Are')
st.write(
            """
            - I love climbing, hiking and camping these outdoor activities. Reached the Annapurna Base Camp in snowstorm conditions
            - I am always interested in traveling(visited 12 countries). This helps me to communicate efficient with people from different cultures, and also allows me to adapt and explore new environments quickly. 
            - I love gardening 🌲 and planting vegetables 🥬. This is really help me to develop my problem solving skills, i have to always to take care them and find out the problems.
            - I like reading and watching videos that introduce and explain the new technology and rare culture. Besides this, I like to read self-improvement and philosophical books which help me to know more about myself.

            """
)