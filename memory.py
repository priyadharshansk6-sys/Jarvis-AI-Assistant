import json
import os

MEMORY_FILE = "C:\\Users\\Priyadharshan\\Jarvis\\memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {
        "name": "Priyadharshan",
        "city": "Chennai",
        "tasks": [],
        "preferences": {}
    }

def save_memory(key, value):
    memory = load_memory()
    memory[key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def get_memory(key):
    memory = load_memory()
    return memory.get(key, None)

def add_task(task):
    memory = load_memory()
    if "tasks" not in memory:
        memory["tasks"] = []
    memory["tasks"].append(task)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def get_tasks():
    memory = load_memory()
    return memory.get("tasks", [])

def clear_tasks():
    save_memory("tasks", [])