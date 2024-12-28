import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
from rich.console import Console

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

        for script in soup.find_all('script'):
            if script.get('src'):
                js_url = urljoin(url, script['src'])
                download_file(js_url, site_name)

        for img in soup.find_all('img'):
            img_url = urljoin(url, img['src'])
            download_file(img_url, site_name)

        console.print("[bold green]Web sayfası başarıyla kopyalandı![/bold green]")
        console.print(f"[bold green]Tüm bileşenler '{site_name}' klasöründe kaydedildi.[/bold green]")
        return True

    except requests.exceptions.RequestException as e:
        with open("Web_Code_Copier_Error.txt", "w", encoding='utf-8') as error_file:
            error_file.write(str(e))
        console.print("[bold red]Hata oluştu:[/bold red]", str(e))
        return False

def main():
    clear_terminal()
    console.print("═" * 77, style="bold red")
    console.print("Kopyalanacak siteyi girin. Çıkmak için E tuşuna basın.", style="bold red")
    console.print("Menüye dönmek için B tuşuna basın.", style="bold red")
    console.print("═" * 77, style="bold red")
    url = console.input("Kopyalanacak Site: ")

    if url.lower() == 'b':
        return  
    if url.lower() == 'e':
        return  

    success = copy_url_content(url)
    if success:
        console.print("[bold green]İçerik ilgili klasöre kaydedildi.[/bold green]")

if __name__ == "__main__":
    main()
