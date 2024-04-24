import streamlit as st
from streamlit_lottie import st_lottie
import os
from PIL import Image
import requests



dir = os.path.dirname(os.path.abspath(__file__))
static = os.path.join(dir,'assets')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# with open(os.path.join(static,'st.css')) as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# print('loaded styling')
# st.sidebar.image(os.path.join(static,'635b055453d8bb5a7852461d_Deloitte-Logo.png'), use_column_width=True)
# st.sidebar.image('https://logos-marques.com/wp-content/uploads/2020/12/Deloitte-logo.png', use_column_width=True)
st.sidebar.image('https://clipartcraft.com/images/deloitte-logo-transparent-4.png', use_column_width=True)
st.title('Welcome to the Document Generation demo')
st.markdown("""<hr style="height:2px;border:none;color:#9ACD66;background-color:#9ACD66;" /> """, unsafe_allow_html=True)
st.write()
st.write("Please click **uploader** on the sidebar to proceed.")
st.write("---")
st.write(""""Welcome to the Deloitte technology benchmarking tool
 
It will analyse technical information about a project and benchmark it against publicly available information. It does this by identifying and documenting readily available technologies and/or solutions that closely match your project from the Internet and describes the specific differences. All information will be analysed and cross-referenced with online sources to provide a complete audit trial. You will receive a customised report, carefully configured to enable you to rapidly understand the current state of technology. The tool can be used to conduct vendor or competitor reviews, business case option analysis, R&D tax claims and more.
 
Simply upload your project information, and let the tool do the rest.""")

# st.write("""The Deloitte Tax and Legal Digital Innovation team has completed the evaluation of the potential for automation and standardisation opportunities using AI to expedite the report generation process.""")
# st.write("""The goal of exploring these opportunities is to free up more time for our data team to concentrate on focused review and advisory work and explore the application of cutting-edge Artificial Intelligence (AI) solutions to alleviate a significant pain point for the team.""")
# st.write("This is an extremely early phase demonstration of what the tool could look like. It utilises an AutoGPT agent and Google Serper API and is written in Python.")
# with col2:
#     lottie_hello = load_lottieurl("https://cdnl.iconscout.com/lottie/premium/preview-watermark/ai-7299861-5975354.mp4?h=700")
#     st_lottie(lottie_hello, key="hello")