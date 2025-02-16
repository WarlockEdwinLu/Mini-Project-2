# Import the necessary libraries
import streamlit as st
from openai import OpenAI  # TODO: Install the OpenAI library using pip install openai

st.title("Mini Project 2: Streamlit Chatbot")

# TODO: Replace with your actual OpenAI API key
# Allow the user to enter their OpenAI API key
if "openai_key" not in st.session_state:
    st.session_state["openai_key"] = ""

st.session_state["openai_key"] = st.text_input("Enter your OpenAI API Key:", type="password")

if not st.session_state["openai_key"]:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()

client = OpenAI(api_key=st.session_state["openai_key"])

# Define a function to get the conversation history (Not required for Part-2, will be useful in Part-3)
def get_conversation() -> str:
    # return: A formatted string representation of the conversation.
    # ... (code for getting conversation history)
    return "\n".join(f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages)

# Check for existing session state variables
if "openai_model" not in st.session_state:
    # ... (initialize model)
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    # ... (initialize messages)
    st.session_state["messages"] = []

# Display existing chat messages
# ... (code for displaying messages)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Wait for user input
if prompt := st.chat_input("What would you like to chat about?"):
    # ... (append user message to messages)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ... (display user message)
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        # ... (send request to OpenAI API)
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messages
        )

        # ... (get AI response and display it)
        ai_message = response.choices[0].message.content
        st.markdown(ai_message)

    # ... (append AI response to messages)
    st.session_state.messages.append({"role": "assistant", "content": ai_message})