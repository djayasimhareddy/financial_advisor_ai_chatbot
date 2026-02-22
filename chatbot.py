import logging
from google import genai
from config import get_api_key
from prompts import SYSTEM_PROMPT

# Configure production-grade logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("GeminiChatbot")

def initialize_gemini():
    try:
        logger.info("Initializing Gemini API client...")
        client = genai.Client(api_key=get_api_key())
        
        logger.info("Creating chat session with system instructions...")
        chat_session = client.chats.create(
            model="gemini-2.5-flash",
            config=genai.types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7,
                max_output_tokens=2048,
            )
        )
        logger.info("Chat session initialized successfully.")
        return client, chat_session
        
    except Exception as e:
        logger.error(f"Failed to initialize Gemini API: {e}")
        raise