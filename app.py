import os
import PyPDF2 as pdf
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load the environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Smart Application Tracking System", page_icon=":robot:")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://e0.pxfuel.com/wallpapers/219/656/desktop-wallpaper-purple-color-background-best-for-your-mobile-tablet-explore-color-cool-color-colored-background-one-color-aesthetic-one-color.jpg");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#Prompt Template
input_prompt="""
You are a skilled and very experience ATS(Application Tracking System) with a deep understanding of tech field,software engineering,
data science ,data analyst, and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide best assistance for improving thr resumes. 
Assign the percentage Matching based on Job description and the missing keywords with high accuracy
Resume:{extracted_text}
Description:{jd}

I want the only response in 3 sectors as follows:
• Job Description Match: \n
•  MissingKeywords: \n
• Profile Summary: \n
"""

## streamlit app
st.title("SMART APPLICATION TRACKING SYSTEM")
st.text("Improve Your Resume ATS Score")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        reader=pdf.PdfReader(uploaded_file)
        extracted_text=""
        for page in range(len(reader.pages)):
            page=reader.pages[page]
            extracted_text+=str(page.extract_text())
        response = model.generate_content(input_prompt)
        st.write(response.text)