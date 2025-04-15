import streamlit as st

def is_blacklisted(password):
    blacklist = ['password', '123456', '12345678', 'qwerty', 'abc123', 'password123', '111111', 'admin']
    return password.lower() in blacklist

def check_password_strength(password):
    score = 0
    feedback = []

    if is_blacklisted(password):
        feedback.append("❌ This password is too common. Choose something more unique.")
        return 1, feedback

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
        
    return score, feedback

def strength_label(score):
    if score == 4:
        return "Strong", "✅ Strong Password!"
    elif score == 3:
        return "Moderate", "⚠️ Moderate Password - Consider improving."
    else:
        return "Weak", "❌ Weak Password - Improve it using the suggestions below."

st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Meter")
st.write("Evaluate your password based on security best practices.")

# Password Input
password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    label, message = strength_label(score)

    st.markdown(f"### Strength: **{label}**")
    st.info(message)
