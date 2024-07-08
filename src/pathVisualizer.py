import os
import sys
from colorama import Fore, Style, init
from pathlib import Path


def is_hidden_or_system(item_name):
    system_names = ['__pycache__']
    return item_name.startswith('.') or item_name in system_names


def visualize_dir_structure(path, depth=1):
    if not os.path.exists(path):
        print(f"{Fore.RED}Error: {path} does not exist{Style.RESET_ALL}")
        return
    if not os.path.isdir(path):
        print(f"{Fore.RED}Error: {path} is not a directory{Style.RESET_ALL}")
        return

    items = os.listdir(path)
    items.sort()
    for item in items:
        if is_hidden_or_system(item):
            continue
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"{'    ' * (depth if depth else 0)}{Fore.BLUE}{item}/{Style.RESET_ALL}")
            visualize_dir_structure(item_path, depth + 1)
        elif os.path.isfile(item_path):
            print(f"{'    ' * (depth if depth else 0)}{Fore.GREEN}{item}{Style.RESET_ALL}")


if __name__ == "__main__":
    init()
    if len(sys.argv) < 2:
        print("Usage: python script.py <path>")
        sys.exit(1)
    directory_path = sys.argv[1]
    print(f"{Fore.BLUE}{Path(directory_path).name}/{Style.RESET_ALL}")
    visualize_dir_structure(directory_path)