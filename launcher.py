import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from preprompt import preprompt

st.set_page_config(layout="wide")


if 'openai_api_key' not in st.session_state:
    st.session_state['openai_api_key'] = ''

st.sidebar.title("Configuration")
st.session_state['openai_api_key'] = st.sidebar.text_input("Enter your OpenAI API key", type="password")


if st.session_state['openai_api_key']:
    llm = OpenAI(api_key=st.session_state['openai_api_key'], max_tokens=400)

    if 'answer' not in st.session_state:
        st.session_state['answer'] = ''

    def transforming_input_into_answer(user_input):
        prompt = PromptTemplate.from_template(preprompt(user_input))
        chain = prompt | llm
        generated_text = chain.invoke({"user_input": user_input})
        return generated_text

    st.title("Modele 9")

    col1, col2 = st.columns([3, 3])

    with col1: 
        st.header("Template")
        text_data = "Date : / /2024 \n\nDate des faits :  \n\nNom de l'agent :  \n\nFaits :\n- \n- \n"
        user_input = st.text_area("Enter details:", value=text_data, height=300)
        Generate = st.button(label="Generate")

    with col2: 
        st.header("Result")
        if Generate:
            generated_text = transforming_input_into_answer(str(user_input))
            st.session_state['answer'] = generated_text

        st.text_area("Output:", value=st.session_state['answer'], height=300)
        st.button("Export")
else:
    st.warning("Please enter your OpenAI API key in the sidebar to use the app.")