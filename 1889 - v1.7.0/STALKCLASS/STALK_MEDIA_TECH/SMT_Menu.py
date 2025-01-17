import os
import time
import sys
from tqdm import tqdm
from rich.console import Console
from STALKCLASS import Option_S2


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
                    
    Owner License : 1889  |  Author : Vinnie  |  Version : v1.7.0  [bold green]✓[bold red]
                  
    1889 Social Media Stalker [bold green]✓[bold red]
                  
    Everything about remotely monitoring social media platforms.
                  
╠═══════════════════════════════════════════════════════════════════════╣""")

def main():
    clear_terminal()
    loading_animation(100)
    display_banner()
    console.print("\n")


    console.print("[bold red]╠══    [bold yellow]Instagram Dumper\n")

    console.print("    [bold white][ I1 ] [bold yellow]Cooming Soon \n\n")

    console.print("[bold red]╠═══════════════════════════════════════════════════════════════════════╣\n")

    console.print("    [bold white][ B ] [bold red]Back")
    console.print("    [bold white][ E ] [bold red]Exit Client\n")
    
    console.print("[bold red]╚═══════════════════════════════════════════════════════════════════════╝\n") 
    choice = console.input("").strip().lower()


    if choice == 'b':
        Option_S2.main()
    elif choice == 'e':
        clear_terminal()
        console.print("[bold red]Logged Out")
        sys.exit(0)
    else:
        main()

if __name__ == "__main__":
    main()