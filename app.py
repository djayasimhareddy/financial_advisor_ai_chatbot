import streamlit as st
from chatbot import initialize_gemini

# Page Configuration
st.set_page_config(page_title="AI Financial Advisor", page_icon="💰", layout="centered")

# Header and Description
st.title("Financial Advisor")
st.write("Welcome! I'm here to help you understand personal finance, budgeting, and investment concepts.")
st.info("Disclaimer: I provide educational financial information, not certified or legally binding investment advice.")

# Initialize AI client and chat session in Streamlit state
if "client" not in st.session_state or "chat_session" not in st.session_state:
    try:
        client, chat_session = initialize_gemini()
        st.session_state.client = client
        st.session_state.chat_session = chat_session
    except Exception as e:
        st.error(f"Failed to initialize chatbot: {e}")
        st.stop()

# Initialize UI message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for role, text in st.session_state.messages:
    avatar = "👤" if role == "user" else "🏦"
    with st.chat_message(role, avatar=avatar):
        st.markdown(text)

# Chat input
user_input = st.chat_input("E.g., Can you explain the difference between a mutual fund and an ETF?")

if user_input:
    # 1. Save and display user message
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # 2. Get and stream AI response
    with st.chat_message("assistant", avatar="🏦"):
        try:
            chat = st.session_state.chat_session
            
            # Use send_message_stream for real-time rendering
            response_stream = chat.send_message_stream(user_input)
            
            # Streamlit automatically handles the generator for a typing effect
            bot_reply = st.write_stream(
                chunk.text for chunk in response_stream if chunk.text
            )
            
            # Save the complete message to UI history
            st.session_state.messages.append(("assistant", bot_reply))
            
        except Exception as e:
            st.error(f"An API error occurred: {e}")