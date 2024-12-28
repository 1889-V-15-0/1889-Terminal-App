import os
import shutil
from rich.console import Console

console = Console()

def clear_pycache():
    for dirpath, dirnames, filenames in os.walk('.'):
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
            except Exception:
                pass

if __name__ == "__main__":
    clear_pycache()
    console.print("[bold green]1889 Terminal App Trash cleaned")
