import os
import time
import sys
import importlib
from tqdm import tqdm
from rich.console import Console
from SECURITYCLASS.LINK_TEST import Link_Dedector
from SECURITYCLASS.DDOS_DEDECTOR import Ddos_Dedector

modul_1889 = importlib.import_module("1889")

console = Console()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration):
    console.print("[green]Loading...")
    with tqdm(range(duration), bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", colour='green') as pbar:
        for _ in pbar:
            time.sleep(0.010)
    clear_terminal()

def display_banner():
    console.print(r"""
[bold red]
╔═══════════════════════════════════════════════════════════════════════╗

    ┓┏┓┏┓┏┓
    ┃┣┫┣┫┗┫
    ┻┗┛┗┛┗┛
       
    Owner License : 1889  |  Author : Vinnie  |  Version : v1.7.0  [bold green]✓[bold red]
╠═══════════════════════════════════════════════════════════════════════╣""")

def main():
    clear_terminal()
    loading_animation(100)
    display_banner()
    console.print("\n")

    console.print("[bold red]╠══    [bold blue] DEDECTORS\n")

    console.print("    [bold white][ D1 ] [bold blue]Link Dedector")
    console.print("    [bold white][ D2 ] [bold blue]DDoS Dedector [bold white]\n\n")


    console.print("[bold red]╠═══════════════════════════════════════════════════════════════════════╣\n")

    console.print("    [bold white][ B ] [bold red]Back Main")
    console.print("    [bold white][ E ] [bold red]Exit Client\n")

    console.print("[bold red]╚═══════════════════════════════════════════════════════════════════════╝\n")
     
    choice = console.input("").strip().lower()

    if choice == 'd1':
        Link_Dedector.main()
    if choice == 'd2':
        Ddos_Dedector.main()
    elif choice == 'b':
        modul_1889.main()
    elif choice == 'e':
        clear_terminal()
        console.print("[bold red]Logged Out")
        sys.exit(0)
    else:
        main()

if __name__ == "__main__":
    main()