import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AutoSage - AI Vehicle Expert")

st.title("AutoSage - AI Vehicle Expert")
st.write("Upload a vehicle image to generate a detailed automotive report.")

uploaded_file = st.file_uploader(
    "Upload Vehicle Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, width="stretch")

if st.button("Analyze Vehicle"):

    if uploaded_file is None:
        st.warning("Please upload a vehicle image first.")
    else:

        prompt = """
        Analyze this vehicle image and provide:

        Brand:
        Model:
        Vehicle Type:
        Engine Capacity:
        Mileage:
        Fuel Type:
        Key Features (Top 3):
        Estimated Price Range in INR:
        Maintenance Advice:
        Resale Value after 10 years:
        """

        response = model.generate_content(
            [prompt, image]
        )

        st.subheader("📊 Vehicle Analysis Report")
        st.write(response.text)
