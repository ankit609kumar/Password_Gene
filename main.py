import streamlit as st
import random
import string

# Set page config
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔒",
    layout="centered"
)

# Title and description
st.title("🔒 Password Generator")
st.write("Generate secure passwords with customizable options")

# Sidebar for options
with st.sidebar:
    st.header("Options")
    length = st.slider("Password Length", min_value=8, max_value=50, value=12)
    
    st.subheader("Character Types")
    use_uppercase = st.checkbox("Uppercase Letters (A-Z)", value=True)
    use_lowercase = st.checkbox("Lowercase Letters (a-z)", value=True)
    use_numbers = st.checkbox("Numbers (0-9)", value=True)
    use_special = st.checkbox("Special Characters (!@#$%^&*)", value=True)

# Generate password based on selected options
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    chars = ""
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    
    if not chars:
        st.error("Please select at least one character type!")
        return None
    
    return ''.join(random.choice(chars) for _ in range(length))

# Generate and display password
if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
    if password:
        st.success("Your generated password:")
        st.code(password, language="text")
        
        # Copy to clipboard button
        st.button("Copy to Clipboard", on_click=lambda: st.write("Password copied to clipboard!"))