import os
import time
from tqdm import tqdm
from rich.console import Console
from pathlib import Path
import sys
from SECURITY import Option_S1
from STALKCLASS import Option_S2

console = Console()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration):
    console.print("[green]Loading...")
    for _ in tqdm(range(duration), bar_format="{l_bar}{bar}|", colour='green'):
        time.sleep(0.010)
    clear_terminal()

def display_banner():
    console.print(r"""
[bold red]
═════════════════════════════════════════════════════════════════════════

  _____  ________  ________  ________     
 / __  \|\   __  \|\   __  \|\  ___  \    
|\/_|\  \ \  \|\  \ \  \|\  \ \____   \   
\|/ \ \  \ \   __  \ \   __  \|____|\  \  
     \ \  \ \  \|\  \ \  \|\  \  __\_\  \ 
      \ \__\ \_______\ \_______\|\_______\
       \|__|\|_______|\|_______|\|_______|      

Owner License : 1889   /   Author : Vinnie   /   Version : v1.0.0  
═════════════════════════════════════════════════════════════════════════""")

def main():
    while True:
        clear_terminal()
        loading_animation(100)
        display_banner()
        console.print("\n")

        console.print("[bold red]══ [bold blue]SECURITY\n")
        console.print("[bold blue][ S1 ] Start 1889 Security Tech\n\n")

        console.print("[bold red]══ [bold yellow]STALK CLASS\n")
        console.print("[bold yellow][ S2 ] Start 1889 Stalk Class Tech\n\n")

        console.print("[bold red]════\n")
        console.print("[bold red][ E ] Exit Client\n")

        console.print("[bold red]If you want to clean up trash files, use the 'e' option, and then type 'py Clean.py' or 'python Clean.py' in the terminal.")
        console.print("[bold red]This will remove some junk files created by the software and free up space on your device.\n")

        console.print("[bold red]════════════════════════════════════════════════════════════════════════")

        choice = console.input("").strip().lower()

        if choice == 's2':
            Option_S2.main()
        elif choice == 's1':
            Option_S1.main()
        elif choice == 'e':
            clear_terminal()
            console.print("[bold red]Logged Out")
            sys.exit(0)

if __name__ == "__main__":
    main()
