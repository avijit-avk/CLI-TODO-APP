"""
╔══════════════════════════════════════╗
║        CLI To-Do Application         ║
║  Tasks saved automatically to JSON   ║
╚══════════════════════════════════════╝
"""

import json
import os
import sys
from datetime import datetime

# ─────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────
DATA_FILE = "tasks.json"

# ANSI colour codes
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"

BLACK  = "\033[30m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"

BG_BLUE  = "\033[44m"
BG_CYAN  = "\033[46m"


# ─────────────────────────────────────────────
#  JSON PERSISTENCE
# ─────────────────────────────────────────────
def load_tasks() -> list:
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_tasks(tasks: list) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def next_id(tasks: list) -> int:
    return max((t["id"] for t in tasks), default=0) + 1


# ─────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(f"\n{BOLD}{CYAN}{'─' * 44}{RESET}")
    print(f"{BOLD}{CYAN}   ✅  CLI To-Do App  •  tasks saved to JSON{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 44}{RESET}\n")


def print_tasks(tasks: list):
    if not tasks:
        print(f"  {DIM}No tasks yet. Add one below!{RESET}\n")
        return

    print(f"  {BOLD}{WHITE}{'ID':<5} {'STATUS':<12} {'ADDED':<14} TASK{RESET}")
    print(f"  {DIM}{'─' * 60}{RESET}")

    for t in tasks:
        tid     = t["id"]
        done    = t["done"]
        title   = t["title"]
        added   = t.get("added", "")[:10]   # YYYY-MM-DD

        if done:
            status  = f"{GREEN}✔ Done{RESET}"
            title_s = f"{DIM}{title}{RESET}"
        else:
            status  = f"{YELLOW}○ Pending{RESET}"
            title_s = f"{WHITE}{title}{RESET}"

        print(f"  {CYAN}{tid:<5}{RESET} {status:<20} {DIM}{added:<14}{RESET} {title_s}")

    total   = len(tasks)
    done_n  = sum(1 for t in tasks if t["done"])
    pending = total - done_n
    print(f"\n  {DIM}Total: {total}  •  {GREEN}Done: {done_n}{RESET}{DIM}  •  {YELLOW}Pending: {pending}{RESET}")


def menu():
    print(f"\n  {BOLD}What would you like to do?{RESET}")
    print(f"  {CYAN}[1]{RESET} ➕  Add a task")
    print(f"  {CYAN}[2]{RESET} 🗑  Delete a task")
    print(f"  {CYAN}[3]{RESET} ✔  Mark task as done / undone")
    print(f"  {CYAN}[4]{RESET} 🔍  View all tasks")
    print(f"  {CYAN}[0]{RESET} 🚪  Quit\n")


def prompt(text: str) -> str:
    return input(f"  {BOLD}{BLUE}▶ {text}{RESET}").strip()


def success(msg: str):
    print(f"\n  {GREEN}✔  {msg}{RESET}")


def error(msg: str):
    print(f"\n  {RED}✖  {msg}{RESET}")


def info(msg: str):
    print(f"\n  {CYAN}ℹ  {msg}{RESET}")


# ─────────────────────────────────────────────
#  ACTIONS
# ─────────────────────────────────────────────
def add_task(tasks: list):
    print(f"\n  {BOLD}── Add New Task ──{RESET}")
    title = prompt("Task title: ")
    if not title:
        error("Task title cannot be empty.")
        return

    task = {
        "id":    next_id(tasks),
        "title": title,
        "done":  False,
        "added": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    success(f'Task #{task["id"]} "{title}" added!')


def delete_task(tasks: list):
    if not tasks:
        error("No tasks to delete.")
        return

    print(f"\n  {BOLD}── Delete Task ──{RESET}")
    print_tasks(tasks)

    raw = prompt("Enter task ID to delete (or 'all' to clear): ")

    if raw.lower() == "all":
        confirm = prompt("Delete ALL tasks? (yes/no): ")
        if confirm.lower() in ("yes", "y"):
            tasks.clear()
            save_tasks(tasks)
            success("All tasks deleted.")
        else:
            info("Cancelled.")
        return

    if not raw.isdigit():
        error("Please enter a valid numeric ID.")
        return

    tid = int(raw)
    match = next((t for t in tasks if t["id"] == tid), None)
    if not match:
        error(f"No task found with ID {tid}.")
        return

    tasks.remove(match)
    save_tasks(tasks)
    success(f'Task #{tid} "{match["title"]}" deleted.')


def toggle_task(tasks: list):
    if not tasks:
        error("No tasks available.")
        return

    print(f"\n  {BOLD}── Mark Done / Undone ──{RESET}")
    print_tasks(tasks)

    raw = prompt("Enter task ID to toggle: ")
    if not raw.isdigit():
        error("Please enter a valid numeric ID.")
        return

    tid = int(raw)
    match = next((t for t in tasks if t["id"] == tid), None)
    if not match:
        error(f"No task found with ID {tid}.")
        return

    match["done"] = not match["done"]
    state = "Done ✔" if match["done"] else "Pending ○"
    save_tasks(tasks)
    success(f'Task #{tid} marked as {state}')


# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────
def main():
    tasks = load_tasks()

    while True:
        clear()
        banner()
        print_tasks(tasks)
        menu()

        choice = prompt("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            clear()
            banner()
            print_tasks(tasks)
        elif choice == "0":
            print(f"\n  {CYAN}👋  Goodbye! Your tasks are saved.{RESET}\n")
            sys.exit(0)
        else:
            error("Invalid option. Please choose 0–4.")

        input(f"\n  {DIM}Press Enter to continue…{RESET}")


if __name__ == "__main__":
    main()