from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ----- Use local CSS -----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ----- LOAD ASSETS -----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
largest_logistics_companies = Image.open("images/largest_logistics_companies.png")
img_lottie_animation = Image.open("images/at_contact_form.png")

# ----- HEADER SECTION -----

with st.container():
    st.subheader("Hi, I am Adil Ahmadzada :wave:")
    st.title("BDM Expert and Lean Six Sigma Professional")
    st.write("I've been working with international business development"
             "and consulting service companies for many years in more "
             "than 20 industrial sectors. I wanna share My deep talent,\n "
             "\nknowledge and experience with you.")
    st.write("[Learn more >](https://adilahmadzada.dorik.io/)")

#----- WHAT I DO -----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write('##')
        st.write(
            """
            In my professional business activities I offer you these services:
            - I help you to extend your business market in the world
            - I develop new business projects and explore potential business regions
            - I bring you potential busienss partner, customer and opportunities
            - I apply new innovative business methodologies to improve your sustainability
            - I help you in investment, EPC services, logistics, manufacturing sectors
            
            If you need any help to extend your company market and to improve your business,
            just feel free to contact with me.
            """
        )
        st.write("[Learn more >](https://adilahmadzada.dorik.io/)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ----- PROJECTS -----
with st.container():
    st.write("-----")
    st.header("My Projects")
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
       st.image(img_lottie_animation)
    with text_column:
        st.subheader("Investment and EPC services")
        st.write(
            """
            I offer you Investment & EPC services:
            - Potential investment projects and funded projects
            - Potential investment projects
            - Developing potential projects
            """
        )
        st.markdown("[Learn more >](https://adilahmadzada.dorik.io/)")

with st.container():
    st.write("-----")
    st.header("My Projects")
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
       st.image(largest_logistics_companies)
    with text_column:
        st.subheader("Warehouse and Logistics")
        st.write(
            """
            I offer you Warehouse & Logistics:
            - We open new warehouse for our customers
            - We deliver products to local and foreign customers
            - We do ship repair, vessel maintenance, ship transportation
            """
        )
        st.markdown("[Learn more >](https://adilahmadzada.dorik.io/)")


# -----CONTACT -----
with st.container():
    st.write("-----")
    st.header("Get In Touch With Me")
    st.write('##')
    contact_form = """
    <form action="https://formsubmit.co/adilahmadzada5@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
