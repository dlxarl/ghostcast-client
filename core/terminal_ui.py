from colorama import Fore, Style, init
from aioconsole import aprint

init(autoreset=True)

class TerminalUI:
    @staticmethod
    def log_info(msg):
        print(f"{Fore.YELLOW}[SYSTEM]{Style.RESET_ALL} {msg}")

    @staticmethod
    def log_error(msg):
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {msg}")

    @staticmethod
    async def log_chat_message(msg):
        await aprint(f"{Fore.CYAN}[CHAT]{Style.RESET_ALL} {msg}")