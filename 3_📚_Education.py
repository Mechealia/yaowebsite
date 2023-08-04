import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Qiyao Education",
    page_icon="👩‍🎓",
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
        st.header('👩‍🎓 My Education')
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
        with open("education2.json") as source:
            education2 = json.load(source)
        st_lottie(education2)





st.subheader("French Language Courses – Université Bordeaux-Montaigne")
st.info('''
Bordeaux, France: Sep 2022 - May 2023
- French Intermediate Courses
''')

st.subheader("Master of Science – Global Supply Chain Management (ISLI)   KEDGE Business School")
st.info('''
Bordeaux, France: Sep 2018 - Apr 2020
- 1st (France) and 5th (worldwide) Project in Supply Chain and Logistics
- Sourcing and inventory management(MRP/ BOM/ JIT / ASRS), line management, Project management, Logistics(Incoterms / Demand planning / order fulfillment )
- Company project:Designed and deployed new business model for shipping company using new energy for transportation
''')

st.subheader("Bachelor – Administrative Management                        Harbin Normal University")
st.info('''
Harbin, China: Sep 2014 - Jun 2018
- Business Negotiation, Marketing, International Trade, Business Etiquette
''')