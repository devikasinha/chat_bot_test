# 🤖 Google Gemini Chatbot with LangChain & Streamlit
A conversational AI chatbot built using **Google Gemini (via LangChain)** and **Streamlit**.  
The chatbot remembers past interactions, giving context-aware answers in real time.
it stores he history of thr past conversations.
---
## ✨ Features
- ⚡ Powered by **Google Gemini (1.5 Flash / Pro)**
- 🧠 Conversation memory (remembers previous chats)
- 🎨 Simple web interface with **Streamlit**
- 🔑 Easy setup with `.env` or Streamlit **Secrets**
- 🚀 Ready to deploy on **Streamlit Cloud**
---
## 📦 Installation, Setup & Run
```bash
# 1. Clone the repository
git clone https://github.com/your-username/gemini-chatbot.git && cd gemini-chatbot
```
---
2. Create and Activate a Virtual Environment (optional but recommended)
Windows (PowerShell):
```bash
python -m venv venv ; venv\Scripts\activate
```
---
3. Install Dependencies
```bash   
pip install -r requirements.txt
```
---
⚙️ Setup API Key

Get your Google API Key from Google AI Studio
.
Create a .env file in your project root:
GOOGLE_API_KEY=your_google_api_key_here
---
▶️ Run Locally

streamlit run chat.py
Then open 👉 http://localhost:8501
---
🚀 Deploy on Streamlit Cloud
Push this repo to GitHub.
Go to Streamlit Cloud
 → New App → Connect your repo.
Add your Google API Key in Streamlit Secrets:
# Streamlit Cloud → Settings → Secrets
GOOGLE_API_KEY="your_google_api_key_here"
Deploy and start chatting 🎉
📂 Project Structure
├── chat.py          # Main Streamlit chatbot app
├── .env             # Local environment variables (not pushed to GitHub)
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
🛠 Requirements
Dependencies listed in requirements.txt:
streamlit
python-dotenv
langchain
langchain-core
langchain-community
langchain-google-genai
Install them with:
pip install -r requirements.txt
