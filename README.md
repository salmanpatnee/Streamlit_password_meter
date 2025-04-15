
# 🔐 Password Strength Meter - Streamlit App

A simple and user-friendly password strength meter built with Python and Streamlit. This app evaluates the strength of user-entered passwords and provides real-time feedback and suggestions for improvement.

## 🌟 Features

- ✅ Real-time password strength evaluation
- ✅ Feedback on missing security criteria
- ✅ Strong password suggestion generator
- ✅ Blacklist of common weak passwords
- ✅ Clean, minimal user interface with Streamlit

## 🧠 Password Strength Criteria

A strong password must:

- Be **at least 8 characters long**
- Contain **both uppercase and lowercase letters**
- Include **at least one digit (0–9)**
- Include **at least one special character** (!@#$%^&*)
- Not be a common password like `password123`

## 📊 Scoring System

| Score | Strength  | Feedback                             |
|-------|-----------|--------------------------------------|
| 1–2   | Weak      | Missing several security features    |
| 3     | Moderate  | Missing 1–2 features                 |
| 4     | Strong    | Meets all security best practices    |

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/password-strength-meter.git
cd password-strength-meter
```

### 2. Install Requirements

Make sure you have Python installed (3.7+ recommended).

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run password_strength_app.py
```

## 📦 File Structure

```
📁 password-strength-meter
├── password_strength_app.py    # Main Streamlit app
├── README.md                   # This file
├── requirements.txt            # Dependencies
```

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

## 💡 Future Enhancements

- 🔒 Visual progress bar for strength
- 🔄 Toggle password visibility
- 📋 Copy suggested password to clipboard

## 📃 License

MIT License - feel free to use and modify!

---

Made with ❤️ using Streamlit.
