# Install required packages if not installed:
# pip install streamlit ollama beautifulsoup4 requests

import streamlit as st
import requests
from bs4 import BeautifulSoup
import ollama  # Ollama's Python client

# Function to fetch and parse website content
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

class Website:
    def __init__(self, url):
        """
        Fetch and parse the webpage using BeautifulSoup.
        """
        self.url = url
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"

        # Remove unwanted elements
        for tag in soup(["script", "style", "img", "input"]):
            tag.decompose()

        self.text = soup.get_text(separator="\n", strip=True)

# Prompt Templates
system_prompt = "You are an assistant that summarizes website content. Ignore navigation, ads, or unrelated content. Respond concisely in Markdown."

def user_prompt_for(website):
    return f"""You are viewing a website titled: {website.title}.
The content is as follows:
{website.text}

Please summarize this website clearly in Markdown format.
"""

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# Summarize Function using Ollama
def summarize(url):
    website = Website(url)
    messages = messages_for(website)

    # Call Ollama local server
    response = ollama.chat(
        model='llama3',  # Change to your local model if needed
        messages=messages
    )
    return response['message']['content']

# -------------------- Streamlit App --------------------

st.set_page_config(page_title="Website Summarizer using Ollama", page_icon="🔍")
st.title("🌐 Website Summarizer (Ollama)")

url = st.text_input("Enter the Website URL:")

if st.button("Summarize"):
    if url:
        try:
            with st.spinner('Fetching and summarizing...'):
                summary = summarize(url)
            st.markdown("### 📝 Summary:")
            st.markdown(summary)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL.")

st.markdown("---")
st.markdown("⚠️ Note: Ollama server (`ollama serve`) must be running in the background.")
