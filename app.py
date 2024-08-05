import google.generativeai as genai
import streamlit as st
genai.configure(api_key="here enter you gemini api key")

model = genai.GenerativeModel(model_name="gemini-pro")
st.header('Gemini The Pro Coder')
input_prompt="""
Hey Act Like a skilled or very pro code writer if user ask to code write it in very best manner only write code
without including text ,  write only part of code which user can copy using streamlit.code() 
code:{text}
"""

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro') 
    input=st.text_input("Hey enter the question which you want to code ")
    if input:
          response=model.generate_content(input)
          return response.text
    else:
         st.write("Please the enter question to move forward ")



response=get_gemini_repsonse(input_prompt)

if st.button("Get The Answer"):
     if response:
           st.code(response)

     else:
          st.error("enter the question")