import asyncio
import sys
from config import SERVER_URL
from core.socket_client import StreamClient

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <chat_id>")
        sys.exit(1)

    room_id = sys.argv[1]
    full_url = f"{SERVER_URL}{room_id}/"

    client = StreamClient(full_url)

    try:
        asyncio.run(client.start())
    except KeyboardInterrupt:
        print("\nStream stopped by user.")
    except Exception as e:
        print(f"Critical error: {e}")