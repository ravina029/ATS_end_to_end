import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

from dotenv import load_dotenv
load_dotenv() #load all the environmment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##gemini pro response

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text=""
    for page in reader.pages:
        text += str(page.extract_text())
    return text
    """for page in reader(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text"""
    

input_prompt="""
Hey Act like a skilled or very experience ATS(Application Tracking System) with a deep understanding 
of the tech field, software engineering, data science, data analyst, big data engineer, AI engineer,
machine learning engineer, buisnees analyst. Your task is to evaluate the resume based on the given 
job description. You must consider the job market is very competitive and you should provide best 
assistance for improving the resumes. Assign the percentage matching based on the jd (job discription) and the 
missing keywords with high accuracy. be precise with work experience and matching the keywords.
resume: {text}
description: {jd}
be accurate and precise with the outcome, while uploading the same jd and resume maintain the highest accuracy 
by providing consistant ouptput. 
I want the response in one single string having the structure
{{"Job Descritption Match":"%", "Missing Keywords are:[]","Profile Summary":" "}}

"""

## Streamlit appliaction for ATS 
st.title("Amazing Application Tracking System")
st.text("Improve your resume with ATS")

jd=st.text_area("Paste the Job Discription")
uploaded_file=st.file_uploader("Upload your resume",type='pdf',help="Please upload the pdf")
submit=st.button("Submit")

if uploaded_file is not None:
    text=input_pdf_text(uploaded_file)
    response=get_gemini_response(input_prompt)
    st.subheader(response)
