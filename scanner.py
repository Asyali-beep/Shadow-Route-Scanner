import asyncio
import aiohttp
from colorama import Fore, Style, init

init(autoreset=True)

TARGET = "http://127.0.0.1:5000"
WORDLIST_PATH = "wordlists/common.txt"

async def check_endpoint(session, endpoint):
    url = f"{TARGET}{endpoint}"
    try:
        async with session.get(url, timeout=3) as response:
            if response.status == 200:
                print(f"{Fore.RED}[!] VULNERABILITY (No Auth): {url} | Status: 200 OK")
            elif response.status in [401, 403]:
                print(f"{Fore.GREEN}[+] Secure (Protected): {url} | Status: {response.status}")
            elif response.status == 404:
                print(f"{Fore.WHITE}[-] Not Found: {url} | Status: 404")
            else:
                print(f"{Fore.CYAN}[?] Needs Inspection: {url} | Status: {response.status}")
    except Exception as e:
        print(f"{Fore.YELLOW}[?] Connection Error ({url}): Is test_server.py running?")

async def main():
    print(f"{Fore.MAGENTA}--- Shadow Route Scanner (Local Proof of Concept) ---")
    print(f"Target: {TARGET}\n")
    
    try:
        with open(WORDLIST_PATH, "r") as f:
            endpoints = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}Error: '{WORDLIST_PATH}' file not found! Please check the 'wordlists' directory.")
        return

    async with aiohttp.ClientSession() as session:
        tasks = [check_endpoint(session, ep) for ep in endpoints]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    import sys
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    asyncio.run(main())