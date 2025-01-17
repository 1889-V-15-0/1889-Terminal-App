import os
import time
import sys
import importlib
from tqdm import tqdm
from rich.console import Console
from STALKCLASS.COPY_TECH import Web_Code_Copier
from STALKCLASS.STALK_MEDIA_TECH import SMT_Menu

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
    

    console.print("[bold red]╠══    [bold yellow]COPY TECH\n")

    console.print("    [bold white][ C1 ] [bold yellow]Web Code Copier\n\n")

    console.print("[bold red]╠══    [bold yellow]STALK MEDIA TECH\n")

    console.print("    [bold white][ S1 ] [bold yellow]Media Profile Dumper\n\n")


    console.print("[bold red]╠═══════════════════════════════════════════════════════════════════════╣\n")

    console.print("    [bold white][ B ] [bold red]Back Main")
    console.print("    [bold white][ E ] [bold red]Exit Client\n")
    
    console.print("[bold red]╚═══════════════════════════════════════════════════════════════════════╝\n") 
    
    choice = console.input("").strip().lower()

    if choice == 'c1':
        Web_Code_Copier.main()
    if choice == 's1':
        SMT_Menu.main()
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