
from click import command

from voice import speak, listen, random_activation, random_confused
from brain import think, clear_memory
from search import search_web, get_weather
from tasks import *
from wakeword import wait_for_wake_word
from datetime import datetime
import requests
import threading
import time

# ── UPDATE UI STATUS ──────────────────────────────────
def ui(status, active="false", message="", response=""):
    try:
        requests.get(
            f'http://localhost:5000/update/status/{status}',
            timeout=1
        )
        requests.get(
            f'http://localhost:5000/update/active/{active}',
            timeout=1
        )
        if message:
            requests.get(
                f'http://localhost:5000/update/message/{message[:50]}',
                timeout=1
            )
        if response:
            requests.get(
                f'http://localhost:5000/update/response/{response[:50]}',
                timeout=1
            )
    except:
        pass

# ── PARSE SEARCH COMMAND ──────────────────────────────
def parse_search(command):
    # "open youtube search mr beast"
    # "search mr beast on youtube"
    # "find mr beast on youtube"

    platforms = [
        "youtube", "google", "gmail", "github",
        "netflix", "instagram", "twitter",
        "amazon", "flipkart", "maps"
    ]

    # Pattern: "open X search Y"
    for p in platforms:
        if f"open {p}" in command and "search" in command:
            query = command.split("search")[-1].strip()
            return p, query

    # Pattern: "search Y on X" or "find Y on X"
    for p in platforms:
        if f"on {p}" in command:
            query = command.replace("search", "").replace(
                "find", "").replace(f"on {p}", "").strip()
            return p, query

    # Pattern: "youtube search Y"
    for p in platforms:
        if command.startswith(p) and "search" in command:
            query = command.split("search")[-1].strip()
            return p, query

    return None, None

# ── COMMAND ROUTER ────────────────────────────────────
def route_command(command):
    command = command.lower().strip()
    ui("PROCESSING...", "false", command)

    # ── SEARCH ON PLATFORM ────────────────────────────
    platform, query = parse_search(command)
    if platform and query:
        response = search_on(platform, query)
        speak(response)
        ui("TASK COMPLETE", "false", command, response)
        return

    # ── TIME ──────────────────────────────────────────
    if "time" in command:
        r = get_time()
        speak(r)
        ui("ANSWERED", "false", command, r)

    # ── DATE ──────────────────────────────────────────
    elif "date" in command or "today" in command:
        r = get_date()
        speak(r)
        ui("ANSWERED", "false", command, r)

    # ── WEATHER ───────────────────────────────────────
    elif "weather" in command:
        ui("FETCHING WEATHER...", "true")
        r = get_weather("Chennai")
        speak(r)
        ui("ANSWERED", "false", command, r)

    # ── OPEN WEBSITE ──────────────────────────────────
    elif "open" in command and any(
        s in command for s in [
            "youtube", "google", "gmail", "github",
            "netflix", "instagram", "whatsapp",
            "twitter", "chatgpt", "claude"
        ]
    ):
        for site in [
            "youtube", "google", "gmail", "github",
            "netflix", "instagram", "whatsapp",
            "twitter", "chatgpt", "claude"
        ]:
            if site in command:
                r = open_website(site)
                speak(r)
                ui("TASK COMPLETE", "false", command, r)
                break

    # ── OPEN APP ──────────────────────────────────────
    elif "open" in command:
        app = command.replace("open", "").strip()
        r = open_app(app)
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    # ── WEB SEARCH ────────────────────────────────────
    elif any(kw in command for kw in [
        "search", "what is", "who is",
        "how to", "news", "tell me about",
        "explain", "define"
    ]):
        ui("SEARCHING...", "true")
        speak("Searching for that sir.")
        results = search_web(command)
        answer = think(command, extra_context=results)
        speak(answer)
        ui("ANSWERED", "false", command, answer[:50])

   # ── VOLUME CONTROL ────────────────────────────────────
    elif "volume" in command:
    # Extract number from command
     import re
     numbers = re.findall(r'\d+', command)

    if numbers:
        percent = int(numbers[0])
        r = set_volume(percent)
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    elif "up" in command:
        r = volume_up()
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    elif "down" in command:
        r = volume_down()
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    elif "mute" in command:
        r = mute()
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    elif "what" in command or "check" in command:
        r = get_volume()
        speak(r)
        ui("ANSWERED", "false", command, r)

# ── BRIGHTNESS CONTROL ────────────────────────────────
    elif "brightness" in command:
        import re
        numbers = re.findall(r'\d+', command)

    if numbers:
        percent = int(numbers[0])
        r = set_brightness(percent)
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    elif "up" in command or "increase" in command:
        r = brightness_up()
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    elif "down" in command or "decrease" in command:
        r = brightness_down()
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    elif "what" in command or "check" in command:
        r = get_brightness()
        speak(r)
        ui("ANSWERED", "false", command, r)
    # ── SCREENSHOT ────────────────────────────────────
    elif "screenshot" in command:
        r = take_screenshot()
        speak(r)
        ui("TASK COMPLETE", "false", command, r)

    # ── PC CONTROL ────────────────────────────────────
    elif "lock" in command:
        r = lock_pc()
        speak(r)

    elif "shutdown" in command:
        speak("Shutting down the system sir.")
        shutdown_pc()

    elif "restart" in command:
        speak("Restarting sir.")
        restart_pc()

    # ── MEMORY ────────────────────────────────────────
    elif "clear memory" in command:
        clear_memory()
        r = "Memory cleared sir."
        speak(r)
        ui("MEMORY CLEARED", "false", command, r)

    # ── PERSONALITY ───────────────────────────────────
    elif "who are you" in command:
        r = "I am JARVIS sir. Your personal AI assistant."
        speak(r)
        ui("ANSWERED", "false", command, r)

    elif "how are you" in command:
        r = "All systems running perfectly sir."
        speak(r)
        ui("ANSWERED", "false", command, r)

    elif "thank" in command:
        r = "Always at your service sir."
        speak(r)
        ui("ANSWERED", "false", command, r)

    elif "joke" in command:
        ui("THINKING...", "true")
        r = think("Tell me a short funny sarcastic joke")
        speak(r)
        ui("ANSWERED", "false", command, r)

    elif "let's talk" in command or "chat" in command:
        speak("Sure sir. What is on your mind?")
        ui("CONVERSATION MODE", "true")
        for _ in range(5):
            user = listen()
            if user:
                if "stop" in user or "exit" in user:
                    speak("Ending conversation sir.")
                    break
                ui("THINKING...", "true", user)
                reply = think(user)
                speak(reply)
                ui("ANSWERED", "false", user, reply[:50])

    # ── FALLBACK ──────────────────────────────────────
    else:
        ui("THINKING...", "true", command)
        response = think(command)
        speak(response)
        ui("ANSWERED", "false", command, response[:50])

# ── GREETING ──────────────────────────────────────────
def startup_greeting():
    hour = datetime.now().hour
    if hour < 12:
        greet = "Good morning"
    elif hour < 17:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

    speak(f"{greet} sir. JARVIS is online.")
    ui("FETCHING NEWS...", "false")
    speak("Let me get today's AI news for you sir.")

    results = search_web("latest AI news today 2026", max_results=3)
    lines = [l.strip() for l in results.split('\n')
             if len(l.strip()) > 30]
    for line in lines[:2]:
        speak(line[:120])

    speak("All systems ready sir. Say Hey Jarvis to activate.")
    ui("JARVIS ONLINE", "false")

# ── MAIN LOOP ─────────────────────────────────────────
def main():
    threading.Thread(target=startup_greeting, daemon=True).start()

    while True:
        ui("WAITING...", "false")
        wait_for_wake_word()

        ui("LISTENING...", "true")
        random_activation()

        command = listen()

        if command:
            if "goodbye jarvis" in command:
                speak("Goodbye sir. JARVIS going offline.")
                ui("OFFLINE", "false")
                break
            route_command(command)
        else:
            random_confused()
            ui("JARVIS ONLINE", "false")

        time.sleep(0.2)

if __name__ == "__main__":
    main()