
import os
import webbrowser
import subprocess
import pyautogui
from datetime import datetime
import urllib.parse

# ── APP MAP ───────────────────────────────────────────
APP_MAP = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "vs code": "code",
    "file explorer": "explorer.exe",
    "spotify": "spotify.exe",
    "camera": "microsoft.windows.camera:",
    "settings": "ms-settings:",
    "task manager": "taskmgr.exe",
    "paint": "mspaint.exe",
}

# ── WEBSITE MAP ───────────────────────────────────────
WEBSITE_MAP = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "netflix": "https://netflix.com",
    "instagram": "https://instagram.com",
    "whatsapp": "https://web.whatsapp.com",
    "twitter": "https://twitter.com",
    "chatgpt": "https://chatgpt.com",
    "claude": "https://claude.ai",
}

# ── OPEN APP ──────────────────────────────────────────
def open_app(app_name):
    app_name = app_name.lower().strip()
    if app_name in APP_MAP:
        try:
            path = APP_MAP[app_name]
            if path.endswith(':'):
                os.system(f"start {path}")
            else:
                subprocess.Popen(path)
            return f"Opening {app_name} sir."
        except:
            return f"Could not open {app_name} sir."
    return f"I don't know how to open {app_name} sir."

# ── OPEN WEBSITE ──────────────────────────────────────
def open_website(site):
    site = site.lower().strip()
    url = WEBSITE_MAP.get(site, f"https://{site}.com")
    webbrowser.open(url)
    return f"Opening {site} sir."

# ── SEARCH ON PLATFORM ────────────────────────────────
def search_on(platform, query):
    query_encoded = urllib.parse.quote(query)
    platform = platform.lower().strip()

    SEARCH_URLS = {
        "youtube": f"https://www.youtube.com/results?search_query={query_encoded}",
        "google": f"https://www.google.com/search?q={query_encoded}",
        "gmail": f"https://mail.google.com/mail/u/0/#search/{query_encoded}",
        "github": f"https://github.com/search?q={query_encoded}",
        "netflix": f"https://www.netflix.com/search?q={query_encoded}",
        "instagram": f"https://www.instagram.com/explore/tags/{query_encoded}",
        "twitter": f"https://twitter.com/search?q={query_encoded}",
        "amazon": f"https://www.amazon.in/s?k={query_encoded}",
        "flipkart": f"https://www.flipkart.com/search?q={query_encoded}",
        "maps": f"https://www.google.com/maps/search/{query_encoded}",
    }

    url = SEARCH_URLS.get(platform, f"https://www.google.com/search?q={query_encoded}")
    webbrowser.open(url)
    return f"Searching {query} on {platform} sir."

# ── TIME & DATE ───────────────────────────────────────
def get_time():
    return f"It is {datetime.now().strftime('%I:%M %p')} sir."

def get_date():
    return f"Today is {datetime.now().strftime('%A, %B %d, %Y')} sir."

# ── VOLUME ────────────────────────────────────────────
def volume_up():
    for _ in range(5):
        pyautogui.press('volumeup')
    return "Volume increased sir."

def volume_down():
    for _ in range(5):
        pyautogui.press('volumedown')
    return "Volume decreased sir."

def mute():
    pyautogui.press('volumemute')
    return "Muted sir."

# ── SCREENSHOT ────────────────────────────────────────
def take_screenshot():
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    pyautogui.screenshot(f"C:\\Users\\Priyadharshan\\Jarvis\\{filename}")
    return f"Screenshot saved sir."

# ── PC CONTROL ────────────────────────────────────────
def shutdown_pc():
    os.system("shutdown /s /t 5")
    return "Shutting down sir."

def restart_pc():
    os.system("shutdown /r /t 5")
    return "Restarting sir."

def lock_pc():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "PC locked sir."
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

# ── VOLUME BY PERCENTAGE ──────────────────────────────
def set_volume(percent):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL, None
        )
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Convert percent to decibel scale
        if percent == 0:
            volume.SetMasterVolumeLevelScalar(0, None)
        else:
            volume.SetMasterVolumeLevelScalar(percent / 100, None)
        return f"Volume set to {percent} percent sir."
    except:
        # Fallback method
        for _ in range(50):
            pyautogui.press('volumedown')
        presses = int(percent / 2)
        for _ in range(presses):
            pyautogui.press('volumeup')
        return f"Volume set to {percent} percent sir."

def volume_up():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar() * 100
        new = min(100, current + 10)
        volume.SetMasterVolumeLevelScalar(new / 100, None)
        return f"Volume increased to {int(new)} percent sir."
    except:
        for _ in range(5):
            pyautogui.press('volumeup')
        return "Volume increased sir."

def volume_down():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar() * 100
        new = max(0, current - 10)
        volume.SetMasterVolumeLevelScalar(new / 100, None)
        return f"Volume decreased to {int(new)} percent sir."
    except:
        for _ in range(5):
            pyautogui.press('volumedown')
        return "Volume decreased sir."

def get_volume():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = int(volume.GetMasterVolumeLevelScalar() * 100)
        return f"Volume is at {current} percent sir."
    except:
        return "Could not get volume sir."

# ── BRIGHTNESS BY PERCENTAGE ──────────────────────────
def set_brightness(percent):
    try:
        percent = max(0, min(100, percent))
        sbc.set_brightness(percent)
        return f"Brightness set to {percent} percent sir."
    except Exception as e:
        return f"Could not set brightness sir."

def brightness_up():
    try:
        current = sbc.get_brightness()[0]
        new = min(100, current + 10)
        sbc.set_brightness(new)
        return f"Brightness increased to {new} percent sir."
    except:
        return "Could not increase brightness sir."

def brightness_down():
    try:
        current = sbc.get_brightness()[0]
        new = max(0, current - 10)
        sbc.set_brightness(new)
        return f"Brightness decreased to {new} percent sir."
    except:
        return "Could not decrease brightness sir."

def get_brightness():
    try:
        current = sbc.get_brightness()[0]
        return f"Brightness is at {current} percent sir."
    except:
        return "Could not get brightness sir."