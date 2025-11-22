import asyncio
import websockets
import ssl
import certifi
from .video_capture import ScreenCapturer
from .terminal_ui import TerminalUI
from config import FPS_LIMIT


class StreamClient:
    def __init__(self, uri):
        self.uri = uri
        self.capturer = ScreenCapturer()
        self.ui = TerminalUI()

    async def send_video_loop(self, websocket):
        self.ui.log_info("Video stream started...")
        try:
            while True:
                bytes_data = self.capturer.get_frame_bytes()
                await websocket.send(bytes_data)
                await asyncio.sleep(FPS_LIMIT)
        except Exception as e:
            self.ui.log_error(f"Stream error: {e}")

    async def receive_chat_loop(self, websocket):
        self.ui.log_info("Chat connected.")
        try:
            async for message in websocket:
                await self.ui.log_chat_message(message)
        except Exception as e:
            self.ui.log_error(f"Chat error: {e}")

    async def start(self):
        self.ui.log_info(f"Connecting to {self.uri}...")

        ssl_context = ssl.create_default_context(cafile=certifi.where())

        async with websockets.connect(self.uri, ssl=ssl_context) as websocket:
            self.ui.log_info("Conection established. You are sharing your screen.")

            await asyncio.gather(
                self.send_video_loop(websocket),
                self.receive_chat_loop(websocket)
            )