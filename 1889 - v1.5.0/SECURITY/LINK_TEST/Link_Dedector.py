import requests
import os
import time
from rich.console import Console
from tqdm import tqdm
from SECURITY import Option_S1
import sys

console = Console()

suspicious_sites = [
    "grabify", "bit.ly", "tinyurl", "ow.ly", "is.gd", "shorturl.at", "adf.ly", "goo.gl",
    "t.co", "v.gd", "lnkd.in", "short.ly", "clkim.com", "phishers.com"
]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration):
    console.print("[green]Loading...")
    with tqdm(range(duration), bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", colour='green') as pbar:
        for _ in pbar:
            time.sleep(0.010)
    clear_terminal()

def check_for_phishing_content(url):
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        if "input" in response.text and "password" in response.text:
            console.print("[bold red][!] Possible phishing attack: Login form detected!")
            return True
        return False
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red][!] Connection error: {e}")
        return False

def check_redirect(url):
    try:
        response = requests.get(url, allow_redirects=True, timeout=10)
        console.print(f"\n[bold blue]Headers: {response.headers}")

        if len(response.history) > 5:
            console.print("[bold red][!] Too many redirects detected, this may be suspicious!")
        
        if response.history:
            console.print(f"[bold red][!] The URL has {len(response.history)} redirects.")
            for resp in response.history:
                console.print(f"[bold yellow]Redirect {resp.status_code}: {resp.url}")
            console.print(f"[bold green]Final Target URL: {response.url}")

            if any(suspicious_site in response.url.lower() for suspicious_site in suspicious_sites):
                console.print("[bold red][!] This URL redirects to a potential phishing site!")
            else:
                console.print("[bold green][+] Redirect successful, target seems safe.")

            if check_for_phishing_content(response.url):
                console.print("[bold red][!] Possible phishing attack detected!")

        else:
            console.print("[bold green][+] URL is safe and no redirects were made.")

    except requests.exceptions.TooManyRedirects:
        console.print("[bold red][!] Too many redirects, this URL might be malicious.")
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red][!] Connection error: {e}")

def navigate_to(module_name):
    if module_name == "Option_S1":
        Option_S1.main()
    elif module_name == "main":
        main_menu()

def main():
    clear_terminal()
    loading_animation(100)
    clear_terminal()
    
    console.print("[bold red]═════════════════════════════════════════════════════════════════════════\n")
    console.print("[bold red]Please enter the URL you want to check.\n")
    console.print("[bold red]Press 'E' to exit.\n")
    console.print("[bold red]Press 'B' to go back to the menu.\n")
    console.print("[bold red]═════════════════════════════════════════════════════════════════════════\n")
    
    while True:
        url = console.input("").strip()

        if url.lower() == 'b':
            navigate_to("Option_S1")
            break
        if url.lower() == 'e':
            clear_terminal()
            console.print("[bold red]Logged Out[/bold red]")
            sys.exit(0)

        check_redirect(url)

if __name__ == "__main__":
    main()
