import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
from rich.console import Console
from STALKCLASS import Option_S2
import sys
import time

console = Console()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def download_file(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(folder, os.path.basename(urlparse(url).path))
        with open(filename, 'wb') as f:
            f.write(response.content)

def loading_animation(duration):
    console.print("[green]Loading...[/green]")
    with tqdm(range(duration), bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", colour='green') as pbar:
        for _ in pbar:
            time.sleep(0.010)
    clear_terminal()

def copy_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        site_name = urlparse(url).netloc
        make_dir(site_name)

        soup = BeautifulSoup(response.text, 'html.parser')

      
        save_file(response.text, os.path.join(site_name, 'page_content.html'))

    
        for link in soup.find_all('link', rel='stylesheet'):
            css_url = urljoin(url, link['href'])
            download_file(css_url, site_name)

        console.print("[bold green]Web page successfully copied![/bold green]")
        console.print(f"[bold green]All components (HTML & CSS) are saved in the '{site_name}' folder.[/bold green]")

        return True

    except requests.exceptions.RequestException as e:
        console.print("[bold red]An error occurred:[/bold red]", str(e))
        return False

def main():
    clear_terminal()

    loading_animation(100)

    console.print("[bold red]═════════════════════════════════════════════════════════════════════════\n")
    console.print("[bold red]Enter the website to copy.\n") 
    console.print("[bold red]Press 'E' to exit.\n") 
    console.print("[bold red]Press 'B' to return to the menu.\n")
    console.print("[bold red]═════════════════════════════════════════════════════════════════════════\n")

    while True:
        url = console.input("").strip()

        if url.lower() == 'b':
            Option_S2.main()
            break
        if url.lower() == 'e':
            clear_terminal()
            console.print("[bold red]Logged out[/bold red]")
            sys.exit(0)

        success = copy_url_content(url)
        if success:
            console.print("[bold green]Content (HTML & CSS) has been saved in the respective folder.[/bold green]")

if __name__ == "__main__":
    main()
