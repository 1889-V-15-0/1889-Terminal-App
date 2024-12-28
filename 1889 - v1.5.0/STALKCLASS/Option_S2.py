import os
import time
import sys
from tqdm import tqdm
from rich.console import Console
from pathlib import Path
from STALKCLASS.COPY_TECH import Web_Code_Copier

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
    clear_terminal()
    loading_animation(100)
    display_banner()
    
    console.print("\n")
    console.print("[bold red]══ [bold yellow]COPY TECH\n")
    console.print("[bold yellow][ 1 ] Web Code Copier\n\n")

    console.print("[bold red]════\n")
    console.print("[bold red][ E ] Exit Client\n")
    console.print("[bold red][ B ] Back Main\n")
    
    console.print("[bold red]═════════════════════════════════════════════════════════════════════════\n") 
    choice = console.input("").strip().lower()

    if choice == '1':
        Web_Code_Copier.main()
    elif choice == 'b':
        return
    elif choice == 'e':
        clear_terminal()
        console.print("[bold red]Logged Out")
        sys.exit(0)
    else:
        console.print("[bold red]Invalid choice, please try again.")
        main()

if __name__ == "__main__":
    main()
