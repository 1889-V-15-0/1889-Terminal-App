import os
import time
import sys
import collections
from scapy.all import sniff, TCP, UDP, ICMP
from rich.console import Console
from rich.table import Table
from tqdm import tqdm
from SECURITYCLASS import Option_S1
from SECURITYCLASS.DDOS_DEDECTOR import Ddos_Dedector

console = Console()

REQUEST_THRESHOLD = 100
TIME_WINDOW = 10
LOG_FILE = "DDoS_Log.txt"
traffic_data = []

THREAT_LEVELS = {
    'low': 200,
    'medium': 700,
    'high': 1000
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration):
    console.print("[bold green]Loading...[/bold green]")
    with tqdm(range(duration), bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", colour='green') as pbar:
        for _ in pbar:
            time.sleep(0.010)
    clear_terminal()

def log_traffic(data):
    with open(LOG_FILE, "a") as log_file:
        for entry in data:
            log_line = f"{entry['timestamp']}, {entry['ip']}, {entry['protocol']}\n"
            log_file.write(log_line)

def packet_handler(packet):
    if packet.haslayer("IP"):
        protocol = "OTHER"
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        traffic_data.append({
            'ip': packet["IP"].src,
            'timestamp': int(time.time()),
            'protocol': protocol
        })

def detect_ddos():
    current_time = int(time.time())
    filtered_data = [req for req in traffic_data if current_time - req['timestamp'] <= TIME_WINDOW]
    ip_counter = collections.Counter([req['ip'] for req in filtered_data])

    total_requests = len(filtered_data)
    threat_level = "Normal"
    if total_requests > THREAT_LEVELS['high']:
        threat_level = "High"
    elif total_requests > THREAT_LEVELS['medium']:
        threat_level = "Medium"
    elif total_requests > THREAT_LEVELS['low']:
        threat_level = "Low"

    log_traffic(filtered_data)


    table = Table(title="[bold red]DDoS Scan Report", show_lines=True)
    table.add_column("[bold cyan]IP Address", justify="left", style="cyan")
    table.add_column("[bold magenta]Request Count", justify="right", style="magenta")
    table.add_column("[bold yellow]Protocol", justify="center", style="yellow")


    for ip, count in ip_counter.items():
        protocol = next((req['protocol'] for req in filtered_data if req['ip'] == ip), "Unknown")
        table.add_row(ip, str(count), protocol)


    if total_requests > REQUEST_THRESHOLD:
        console.print(f"[bold red][!] Total requests: {total_requests}")
        console.print(f"[bold red][!] Threat Level: {threat_level}")
        console.print(table)
    else:
        console.print(f"[bold green][+] Normal traffic. Total requests: {total_requests}")
        console.print(f"[bold green][+] Threat Level: {threat_level}")
        console.print(table)

def monitor_traffic(duration):
    console.print("\n[bold yellow]Scanning network traffic...[/bold yellow]")
    start_time = time.time()
    while time.time() - start_time < duration:
        sniff(prn=packet_handler, store=False, timeout=1)


    detect_ddos()


    console.print("[bold purple]Take a screenshot")
    time.sleep(5)
    main()

def display_banner():
    console.print(r"""
[bold red]
╔═══════════════════════════════════════════════════════════════════════╗
                  
    Owner License : 1889  |  Author : Vinnie  |  Version : v1.7.0  [bold green]✓[bold red]
                                   
    1889 DDoS Detection [bold green]✓[bold red]
                  
    [bold red]1000 requests for 5 seconds could mean DDoS. Therefore we recommend size 5 for your personal network.
                  
╠═══════════════════════════════════════════════════════════════════════╣""")

def main():
    clear_terminal()
    loading_animation(100)
    display_banner()
    console.print("")

    console.print("    [bold white][B] [bold red]Back")
    console.print("    [bold white][E] [bold red]Exit Client")
    console.print("    [bold white][S] [bold red]Start detection\n")

    console.print("[bold red]╚═══════════════════════════════════════════════════════════════════════╝\n")

    while True:
        input_command = console.input("[bold red]Choose an option :").lower()

        if input_command == 'e':
            clear_terminal()
            console.print("[bold red]Logged out")
            sys.exit(0)

        elif input_command == 's':
            console.print("[bold red]Enter scan duration in seconds:[/bold red]", end=" ")
            duration = input()

            try:
                duration = int(duration)
                if duration > 0:
                    monitor_traffic(duration)
                else:
                    console.print("[bold red]Enter a number greater than zero for the duration.")
            except ValueError:
                console.print("[bold red]Invalid input. Enter a valid number.")

        elif input_command == 'b':
            Option_S1.main()

        else:
            main()

if __name__ == "__main__":
    main()