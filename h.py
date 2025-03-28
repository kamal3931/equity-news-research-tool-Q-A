import streamlit as st
import base64


def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    bg_image = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)


# Call the function with your image path
set_background("fin.jpg")

x = st.text_input("ask question")
st.write(x)