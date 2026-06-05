import webview
import threading
import time
import os
import server

def start_server():
    server.app.run(
        port=5000,
        debug=False,
        use_reloader=False
    )

def start_jarvis():
    time.sleep(4)
    from main import main
    main()

if __name__ == "__main__":
    # 1. Start server
    threading.Thread(
        target=start_server,
        daemon=True
    ).start()
    time.sleep(1)

    # 2. Start JARVIS voice
    threading.Thread(
        target=start_jarvis,
        daemon=True
    ).start()

    # 3. Open UI window
    os.chdir(r'C:\Users\Priyadharshan\Jarvis')
    webview.create_window(
        title="JARVIS",
        url="http://127.0.0.1:5000",
        width=1366,
        height=768,
        frameless=False,
        background_color='#040201'
    )
    webview.start()