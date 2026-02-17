# ✅ CLI To-Do App

A simple and beautiful command-line To-Do application built with Python.
Tasks are automatically saved to a JSON file so they persist between sessions.

---

## 📸 Preview

```
────────────────────────────────────────────
   ✅  CLI To-Do App  •  tasks saved to JSON
────────────────────────────────────────────

  ID    STATUS       ADDED          TASK
  ────────────────────────────────────────────────────────────
  1     ✔ Done       2024-01-15     Buy groceries
  2     ○ Pending    2024-01-15     Finish Python project
  3     ○ Pending    2024-01-16     Read a book

  Total: 3  •  Done: 1  •  Pending: 2

  What would you like to do?
  [1] ➕  Add a task
  [2] 🗑  Delete a task
  [3] ✔  Mark task as done / undone
  [4] 🔍  View all tasks
  [0] 🚪  Quit
```

---

## 🚀 Features

- ➕ Add tasks with a title and automatic timestamp
- 🗑 Delete tasks by ID or clear all at once
- ✔ Mark tasks as done or undone
- 💾 Auto-save to `tasks.json` — tasks survive between sessions
- 🎨 Coloured terminal output for easy reading
- 🐍 No external libraries — pure Python only

---

## 🛠 Requirements

- Python 3.6 or higher

Check your version:
```bash
python --version
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/avijit-avk/CLI-TODO-APP.git
cd CLI-TODO-APP
```

2. **Run the app**
```bash
python cli-todo.py
```

That's it — no installs, no setup!

---

## 📖 Usage

| Option | Action |
|--------|--------|
| `1` | Add a new task |
| `2` | Delete a task by ID (or delete all) |
| `3` | Toggle a task between Done ✔ and Pending ○ |
| `4` | View all tasks |
| `0` | Quit the app |

Tasks are saved automatically to `tasks.json` in the same folder.

---

## 📁 Project Structure

```
CLI-TODO-APP/
│
├── cli-todo.py    # Main application
├── tasks.json     # Auto-generated task storage (git ignored)
├── .gitignore     # Ignores tasks.json
└── README.md      # This file
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit (`git commit -m "Add your feature"`)
5. Push (`git push origin feature/your-feature`)
6. Open a Pull Request

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

Made by **Avijit**
- GitHub: [@avijit-avk](https://github.com/avijit-avk)

---

⭐ If you found this useful, consider giving it a star on GitHub!
