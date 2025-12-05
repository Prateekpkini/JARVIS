import google.generativeai as genai
from dotenv import load_dotenv
import os
GEMINI_API_KEY="AIzaSyBirC9uwxDdkZxHwuG_S2sJQojkXalHyKg"
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
