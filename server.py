from flask import Flask, jsonify, send_file
from search import search_web
import threading

app = Flask(__name__)

# ── SHARED STATE ──────────────────────────────────────
state = {
    "status": "JARVIS ONLINE",
    "active": False,
    "message": "",
    "response": "",
    "action": ""
}

TASKS = [
    "Complete JARVIS project",
    "Study cloud computing",
    "Edit Goa photos",
    "Exercise",
]

cached_news = []

def fetch_news():
    global cached_news
    try:
        results = search_web("latest AI news today 2026", max_results=5)
        lines = [l.strip() for l in results.split('\n')
                if len(l.strip()) > 30]
        cached_news = lines[:5]
    except:
        cached_news = ["Could not fetch news sir."]

@app.route('/')
def home():
    return send_file('jarvis_ui.html')

@app.route('/data')
def data():
    return jsonify({
        "news": cached_news if cached_news else ["Fetching news..."],
        "tasks": TASKS
    })

@app.route('/status')
def status():
    return jsonify(state)

@app.route('/update/<key>/<value>')
def update(key, value):
    state[key] = value if value != "true" and value != "false" else value == "true"
    return jsonify({"ok": True})

def run_server():
    app.run(port=5000, debug=False, use_reloader=False)

if __name__ == "__main__":
    threading.Thread(target=fetch_news).start()
    run_server()
