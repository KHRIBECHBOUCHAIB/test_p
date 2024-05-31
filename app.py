import streamlit as st
from st_paywall import add_auth

# Add detailed logging for debugging
st.write("Starting the app...")

# Print secrets for debugging (remove after debugging)
st.write("Loaded secrets:", st.secrets)  # Temporary debugging line to print secrets

# Add authentication and subscription check
try:
    add_auth(required=True)
    st.write("add_auth executed successfully.")
except Exception as e:
    st.error(f"Error in add_auth: {e}")

# Log session state
st.write("Session state after add_auth: ", st.session_state)

# Check if the user is logged in and subscribed
if st.session_state.get("user_subscribed"):
    st.write("Welcome, you are logged in and subscribed!")
    st.write(f"Your email: {st.session_state.get('email')}")
    
    # Your main app logic goes here
    st.write("This is the main content of your app.")
else:
    st.write("You need to log in and subscribe to access this app.")
