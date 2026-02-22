# 💰 Production-Ready AI Financial Advisor

A highly modular, domain-specific AI chatbot built with Python, Streamlit, and the Google Gemini GenAI API. This project demonstrates real-world AI engineering standards, including strict prompt guardrails, real-time streaming, and separation of concerns.

## 🏗️ System Architecture

The application follows a clean, decoupled architecture:
* **User UI Layer (`app.py`):** A Streamlit interface providing real-time response rendering and session-based chat history.
* **Backend API Layer (`chatbot.py`):** Manages the persistent Gemini client connection, handles token optimization, and logs system events.
* **Prompt Engineering Module (`prompts.py`):** Injects strict, domain-specific instructions preventing the AI from hallucinating legally binding financial advice.
* **Configuration (`config.py` & `.env`):** Securely loads environmental variables to prevent API key leakage.

## ✨ Technical Features
* **Multi-Turn Memory:** Preserves conversational context across interactions.
* **Real-Time Streaming:** Uses `send_message_stream` for immediate user feedback.
* **Token Optimization:** Enforces strict token limits to manage cloud computing costs.
* **Production Guardrails:** Engineered to provide financial *education* while safely declining high-risk speculative requests.

## 🚀 Local Setup Instructions
1. Clone the repository: `git clone <your-github-repo-url>`
2. Navigate to the project directory: `cd <repo-name>`
3. Create a virtual environment: `python -m venv venv`
4. Activate the environment: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install streamlit google-genai python-dotenv`
6. Create a `.env` file and add your key: `GEMINI_API_KEY=your_key_here`
7. Run the application: `streamlit run app.py`