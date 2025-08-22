# J.A.R.V.I.S. Mark 18 – Personal AI Assistant  
**Built with Python | CustomTkinter | Gemini API | ElevenLabs**

Welcome to **JARVIS Mark 18**, a voice-enabled, GUI-based personal AI assistant inspired by Iron Man’s JARVIS — reimagined and developed by **Devansh**. This assistant is smart, stylish, and customizable — perfect for everyday automation, chatting, and cool AI experiments!

---

## ✨ Features

- **Interactive GUI (CustomTkinter)** – Dark-mode friendly, styled with menus and buttons  
- **Voice Control** – Wake word: “Hey Jarvis” (toggleable), voice recognition via SpeechRecognition  
- **Text-to-Speech (TTS)** –  pyttsx3 fallback  
- **Typing Animation** – With random speed + cinematic feel  
- **Live Avatar** – Animated assistant face with memory-efficient GIF loop  
- **Gemini API Integration** – Uses Gemini (Google AI) for chat response generation  
- **Persistent Memory** – Chat logs saved and loaded (`chat_log.txt`)  
- **Notes System** – Add, delete, and list notes  
- **Reminders** – Save + view time-based reminders  
- **Music Control** – Play, pause, skip, shuffle  
- **Web Search(comming soon)** – Smart Gemini + browser-based search fallback  
- **Weather Info(comming soon)** – Get real-time weather info  
- **Calculator & Games (comming soon)** – Utility mode + fun features  
- **Modes System(comming soon)** – Switch between “Fun Mode”, “Productive Mode”, etc.  
- **Modular File Structure** – Easy to understand, maintain, and upgrade  

---

## 🧠 Tech Stack

- **Python 3.12+**
- [CustomTkinter]
- [Gemini API (Google AI)]
- **SpeechRecognition**, **pyttsx3**, **Pillow**, **requests**, **json**, etc.

---

## 📁 Project Structure

```bash
JARVIS/
├── main.py                     # Entry point
├── .env                        # API keys (Gemini, ElevenLabs)
├── requirements.txt            # Install all dependencies
│
├── GUI/  
│   ├── __init__.py                   # GUI system
│   ├── gui_main.py
│   ├── avatar.py
│  #└── themes/
│
├── core/                       # Assistant brain logic
│   ├── commands.py
│   ├── utils.py
│   ├── memory.py
│  #└── modes.py
│
├── features/                   # Functional modules
│   ├── notes.py
│   ├── reminders.py
│   ├── music.py
│  #├── websearch.py
│  #├── calculator.py
│  #└── games.py
│
├── voice/                      # Speech module
│   ├── tts.py
│   ├── stt.py
│  #└── voices/
│
├── api/                        # API integrations
│   ├── gemini.py
│  #└── other_api.py
│
├── DATA/                       # User data
│   ├── notes.json
│   ├── reminders.json
│   ├── chat_log.txt
│  #└── config.json
│
└── assets/                     # Icons, sounds, images
```

⚙️ Setup Instructions
# Clone the repo
git clone https://github.com/....

# Navigate to folder
cd JARVIS-AI

# Install dependencies
pip install -r requirements.txt

# Create your .env or enter in your file
GEMINI_API_KEY=your_gemini_key
ELEVENLABS_API_KEY=your_elevenlabs_key

# Run the assistant
python jarvismain.py



🔒 API Keys Required
Gemini API – for AI chat responses


🧠 Future Plans:-
DevX AI core integration (your own framework)
GUI layout upgrade with animations
Mobile port (Kivy or BeeWare)
Web interface
Plugin support system

🙌 Made by
Devansh Sharma – AI/ML Engineering Student & Developer

Passionate about intelligent systems, DIY tech, and building the next generation of personal AIs.


📫 Connect With Me
GitHub - https://github.com/RootDeveloperDS

LinkedIn -  https://www.linkedin.com/in/devanshsharma987

✉️ Email: developersofroot@gmail.com


📜 License
MIT License — Use, modify, and build on it freely. Attribution appreciated!


