import streamlit as st


st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Meter")
st.write("Evaluate your password based on security best practices.")

# Password Input
password = st.text_input("Enter your password", type="password")

