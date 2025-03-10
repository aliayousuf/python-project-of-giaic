
import streamlit as st  # Import Streamlit for creating the web-based UI
import random  # Import random for generating random choices
import string  # Import string to use predefined character sets
import re  # Import re for regex operations


#Custom CSS 
st.markdown(
    """
    <style>
    /* Full page gradient background */
    .stApp {
        background: linear-gradient(to right, #626F47, #A4B465);  /* Olive Green to Light Olive Green Gradient */
        color: #FFFFFF;  /* White text for better contrast on dark background */
    }

    /* Heading styling */
    h1 {
        font-size: 36px;
        color: #FFFFFF;  /* White for professional appearance */
        font-weight: bold;
        text-align: center;
    }

    h2 {
        color: #FFFFFF;  /* White for subheader text */
    }

    /* Button Styling */
    .stButton>button {
        padding: 12px 25px;
        background-color: #626F47;  /* Olive Green Button */
        color: white;
        border-radius: 8px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #A4B465;  /* Light Olive Green on hover */
    }

    /* Password Strength Feedback */
    .password-feedback {
        color: #F1C40F;  /* Yellow for warnings */
        font-size: 14px;
        font-style: italic;
    }

    .password-success {
        color: #2ECC71;  /* Soft Green for success messages */
        font-weight: bold;
    }

    /* Input Fields */
    .stTextInput>div>input {
        background-color: #FFFFFF;  /* White background for inputs */
        border: 1px solid #BDC3C7;  /* Soft grey border */
        padding: 12px;
        border-radius: 8px;
        font-size: 16px;
        width: 100%;
    }

    /* Slider Styling */
    .stSlider>div>input[type="range"] {
        background-color: #626F47;  /* Olive Green for sliders */
        height: 8px;
        border-radius: 5px;
    }

    /* Additional styling for labels */
    .stTextInput>div>label {
        font-size: 14px;
        color: #FFFFFF;  /* White for labels */
    }

    </style>
    """, unsafe_allow_html=True
)

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += (
            string.punctuation
        )  # Adds special characters (!@#$%^&* etc.) if selected

    # Generate a password by randomly selecting characters based on the length provided
    return "".join(random.choice(characters) for _ in range(length))


def check_password_strength(password):
    score = 0
    feedback = []
    
    # Criteria Checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(" 🔡 Add at least one lowercase letter.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append(" 🔠 Add at least one uppercase letter.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Include at least one digit (0-9).")
    
    
    if re.search(r"[!@#$%^&*(){}[\]<>?~;:,.|_]", password):

      
        score += 1
    else:
        feedback.append(" 🔣 Include at least one special character (!@#$%^&*).")
    
    # Determine Strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    st.subheader(f"Strength: {strength}")
    
    if strength == "Strong":
        st.success("✅ Your password is strong!")
    else:
        st.warning("⚠️ Consider improving your password:")
        for tip in feedback:
            st.write(f"- {tip}")

# Streamlit UI setup for password generator
st.title("🎰 Password Generator")  # Display the app title on the web page

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select password length:", min_value=8, max_value=32, value=12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers")  # Checkbox for numbers (0-9)
use_special = st.checkbox(
    "Include special characters"
)  # Checkbox for special characters (!@#$%^&*)

# Button to generate password
if st.button("🔑Generate Password"):
    password = generate_password(
        length, use_digits, use_special
    )  # Call the password generation function
    st.write(f"Generated Password: `{password}`")  # Display the generated password




