![Banner](https://repository-images.githubusercontent.com/1098981639/3c7e985c-45df-43be-a078-d57ebb82e65e)

# GhostCast Client

**GhostCast Client** is a terminal-based Python application for capturing and broadcasting the desktop screen in real-time. It works in conjunction with the GhostCast server, transmitting the video stream via WebSockets and receiving chat messages directly in the console.

The client is optimized for performance, uses efficient JPEG compression, and operates without a graphical user interface (Headless).

## Features

* **Lightweight Execution:** Runs from the command line without installing heavy software.
* **Screen Capture:** Uses the `mss` library for fast frame capture.
* **Terminal Chat:** Receives messages from viewers and displays them asynchronously.
* **Low Latency:** Optimized pipeline: Grab -> OpenCV Resize/Compress -> WebSocket Send.
* **Stylish UI:** Colored log and chat output thanks to `colorama`.

## Requirements

* Python 3.8+
* Operating System: Windows, macOS, or Linux.

## Installation

1.  **Download the client code:**
    (If you downloaded an archive from a release, simply extract it).

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    
    # Windows:
    venv\Scripts\activate
    
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before running, you need to specify your server address.

1.  Open the `config.py` file.
2.  Change `SERVER_URL` to your deployment address:

```python
# For local testing:
SERVER_URL = "ws://127.0.0.1:8000/ws/room/"

# For production (example):
SERVER_URL = "wss://cast.example.com/ws/room/"