import os
import time
import sys
from tqdm import tqdm
from rich.console import Console
from SECURITY.LINK_TEST import Link_Dedector
from SECURITY.DDOS_DEDECTOR import Ddos_Dedector


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

Owner License : 1889   /   Author : Vinnie   /   Version : v1.5.0   
═════════════════════════════════════════════════════════════════════════""")

def main():
    clear_terminal()
    loading_animation(100)
    display_banner()
    
    console.print("\n")
    console.print("[bold red]══[bold blue] DEDECTORS\n")
    console.print("[bold blue][ 1 ] Link Dedector")
    console.print("[bold blue][ 2 ] DDoS Dedector ( Only Windows/Linux )\n")

    console.print("[bold red]════\n")

    console.print("[bold red][ E ] Exit Client\n")

    console.print("[bold red][ B ] Back Main\n")
    
    console.print("[bold red]═════════════════════════════════════════════════════════════════════════\n") 
    choice = console.input("").strip().lower()

    if choice == '1':
        Link_Dedector.main()
    if choice == '2':
        Ddos_Dedector.main()
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
    