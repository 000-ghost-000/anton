# making a ai agent that can retreve information from a database using mistral ai api key a personalized chatbot
# this is anton a chatbot that can answer any question


import streamlit as st
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

mistral_api_key = os.getenv("MISTRAL_API_KEY")
bot_key= int(os.getenv("ANTON_PASSWORD"))
mistral_api_url = "https://api.mistral.ai/v1/chat/completions"

st.title("ANTON 🤖")
st.caption("An all knowing bot 📖")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {mistral_api_key}"
}
if mistral_api_key:
    def generate_response(user_input):
        data = {
            "model": "mistral-large-latest",
            "messages": user_input,
            "temperature": 0.7
            
    }
        try:
            response = requests.post(mistral_api_url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            st.error(f"Error generating response: {e}")
            return None
    def admin(adminId: int):
        if adminId == bot_key:
            st.title("welcome sir abhishek")
            return True
        else:
            st.error("Unauthorized access")
            return False
    # side bar
    st.sidebar.title("Admin Login")
    admin_id = st.sidebar.text_input("Enter your admin ID",type="password")
    st.sidebar.write("This is a private admin dashboard. Please enter your admin ID to access it.")
    if st.sidebar.button("Login"):
        admin(int(admin_id))
    else:
        st.write("Please login to access the admin dashboard")
    
    # chat sessions
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    query = st.chat_input("Enter a message")
    if query and admin(int(admin_id)):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)
        messages = [
            {"role": "system", "content": "your name is ANTON , you are a helpful assistant that is very smart and can answer any question , you know philosophy and science and math and history and geography and you are a chatbot that can answer any question , you were created by abhishek srivastava , humanize your response and make it less robot like and more human like"},
            {"role": "user", "content": query}
        ]
        with st.spinner("Generating response..."):
            response = generate_response(messages)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

else:
    st.error("Mistral API key not found. Please set the MISTRAL_API_KEY environment variable.")
# Add a footer
st.markdown("---") 
st.write("© abhishek srivastava")