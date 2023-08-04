import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Qiyao CareerPath",
    page_icon="📈",
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
    st.write("---")

    left_column, right_column = st.columns(2)
    with left_column:
        st.header('👩‍💻 Work Experience')
        st.write(
            """
           Hello, here is the list for my educations, check it out! 
           With 4 years education for my bachelor degree of Administrative Management at Harbin Normal University.
           Almost 2 years education for my master degree of Global Supply Chain Management at KEDGE Business School. 
           When I decided back to continue my career, i realised french is a very important skill, so i back to university to improve my it. 
        """
        )
    with right_column:
        import streamlit as st
        import json
        import streamlit.components.v1 as com
        from streamlit_lottie import st_lottie
        with open("officelady.json") as source:
            officelady = json.load(source)
        st_lottie(officelady)



st.subheader("Customer Service Agent – PeopleCert International LTD")
st.info('''
Remote: Dec 2021 - Sep 2022
- Delivered fast, precise and high quality service to customers via live chat, emails and phone calls
- Coordinated over different departments to solve customer facing issues and meet customer needs 
- Coordinated and helped service providers in China region to resolve process conflicts arising from different business processes in the region
- Received multiple monthly high-efficiency employee rewards
''')

st.subheader("Supply Chain Software Analyst – Farheap Solutions")
st.info('''
Nevada, USA(Remote): Aug 2021 - May 2022
- Handled day-to-day software and supply chain related issues faced by the factories 
- Coordinated with engineers and local factory workers to solve software user-friendly interface issues  
- Optimized the coordination of development and facilitated communication
''')

st.subheader("Cyber Security Project Coordinator – Sony Electronics")
st.info('''
Istanbul, Turkey: Sep 2019 - Apr 2021
- Completed 20 security projects: mainly responsible for Sony China & AP regions 
- Cooperated with local engineers, 3rd party software companies and China regions business owners to solve technical and commercial problems faced in the projects
- Worked in data-oriented environment and delivered high quality software projects
- Translated the business security needs into feasible solutions, align the goals, clear road blocks, and ensure smooth execution
''')

st.subheader("Business Executive Assistant – Chongqing Rare Fish Company")
st.info('''
Chongqing, China: Jan 2018 - Jun 2018
- Maintained relationship with suppliers and developed new potential customers 
- Organized events of visiting the fish farm for customers and suppliers
- Organized visiting of supplier's factory for inspecting qualifications of suppliers 
- Assisted for requiring for new supplies and requested for quotations and arranged visiting for new supplies 
      '''  )
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)