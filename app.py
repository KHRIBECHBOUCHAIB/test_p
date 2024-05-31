import streamlit as st
from st_paywall import add_auth

# Print secrets for debugging
st.write(st.secrets)  # Remove this after debugging

# Add authentication and subscription check
add_auth(required=True)

# Check if the user is logged in and subscribed
if st.session_state.get("user_subscribed"):
    st.write("Welcome, you are logged in and subscribed!")
    st.write(f"Your email: {st.session_state.get('email')}")
    st.write("This is the main content of your app.")
else:
    st.write("You need to log in and subscribe to access this app.")
