# JARVIS - Voice-Controlled AI Assistant

A Python app that takes voice commands, pipes them through Groq's llama model, searches the web if needed, and talks back to you—all running locally on Windows.

## Features

- **Voice in, voice out** — Uses Windows speech API
- **Groq backend** — llama-2-70b for responses
- **Web search** — DuckDuckGo when you need current info
- **Web UI** — Flask backend with an animated interface
- **Fast** — Low-latency end-to-end

## Stack

- Python, Flask
- Groq API (llama-2-70b)
- Windows PowerShell speech
- HTML/CSS/JavaScript frontend
- DuckDuckGo API

## Setup

### Prerequisites
- Python 3.8+
- Windows
- Groq API key

### Install & Run

```bash
cd JARVIS-AI-Assistant
pip install -r requirements.txt

# Create .env:
GROQ_API_KEY=your_key

python main.py
```

## How It Works

1. Say something
2. App recognizes it and sends to Groq
3. If you asked something timely, it grabs fresh info from DuckDuckGo
4. Responds with text and voice synthesis

## Structure

- `main.py` — Start here
- `voice_engine.py` — Handles mic and speakers
- `groq_integration.py` — Talks to the AI model
- `search_engine.py` — DuckDuckGo calls
- `flask_app.py` — Web server
- `ui/` — Frontend

## What Works

- Full voice-to-voice pipeline
- Real-time responses from Groq
- Multiple APIs integrated
- Windows speech synthesis

## Want to Add

- Multi-language support
- Custom voice options  
- Conversation memory
- macOS and Linux support
