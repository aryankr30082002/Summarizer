# 📄 README: LLM Summarizer (Dual LLM Approach)

✨ Project Overview

The LLM Summarizer is a Python-based tool that leverages two Large Language Models (LLMs) to summarize any webpage or raw text content.
This dual-LLM approach ensures flexibility and robustness by allowing the user to choose between models based on use-case, cost, or performance.

🔗 Project Repository

LLM Summarizer GitHub Repository:
https://github.com/aryankr30082002/Summarizer/tree/main/Website_summarizer

To clone this repository:

bash
Copy
Edit
git clone https://github.com/aryankr30082002/Summarizer.git
cd Summarizer/Website_summarizer
🚀 Features

✔️ Summarize content via web URL or plain text input.
✔️ Switch between two LLMs (Ollama & Gemini Flash 1.5).
✔️ Clean and human-readable summaries.
✔️ Handles various text formats (articles, blogs, documentation).
✔️ Graceful fallback if one LLM fails.

🏗️ Tech Stack

Python 3.10+

LLM 1: Ollama (Local, Open Source)

LLM 2: Gemini Flash 1.5 (Cloud API-based)

BeautifulSoup4 — For web scraping

Requests — For HTTP requests

dotenv — For API key management

Streamlit/Jupyter (Optional) — For UI/demo purposes

⚙️ Installation

Clone the repository:

bash
Copy
Edit
git clone https://github.com/aryankr30082002/Summarizer.git
cd Summarizer/Website_summarizer
Install dependencies:

nginx
Copy
Edit
pip install -r requirements.txt
Set up your .env file (for Gemini API):

ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
📝 Usage Example

Choose LLM in Code:

python
Copy
Edit
from summarizer import summarize_text, summarize_website

# Use 'ollama' or 'gemini'
summary = summarize_text("Long text here...", model="ollama")
print(summary)

summary = summarize_website("https://example.com", model="gemini")
print(summary)
🔄 LLM Selection Logic

Ollama

Description: Local, free, no API cost, faster for small summaries.

Use Case: Offline or budget-friendly summarization.

Gemini Flash 1.5

Description: Cloud-based (requires API key).

Use Case: When accuracy, creativity, or handling large content is required.

🔍 How Tokenization & Context Window Matter

Both LLMs use token limits.

Gemini Flash 1.5: Context window up to 1 million tokens (depending on API version).

Ollama Local Models: Typically 2K–16K tokens.

Very long text is automatically chunked to fit within these limits if necessary.

⚠️ Limitations

Requires API key for Gemini Flash 1.5.

Ollama model may require sufficient local GPU/CPU resources.

Large documents may need splitting if they exceed the context window size.

💡 Future Plans

Automatic model selection based on input length.

GUI development via Streamlit.

Result comparison between Ollama and Gemini Flash 1.5.

Multi-language summarization support.

👨‍💻 Contributors

Aryan Kumar (Project Creator)

📜 License

MIT License

📝 Quick Summary (For Interview/GitHub Description)

This project implements a dual-LLM summarizer using both local (Ollama) and cloud-based Gemini Flash 1.5 models, offering flexibility in choosing between offline, cost-effective summarization and high-quality cloud summarization.
