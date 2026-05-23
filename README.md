# 🐾 mew

A cute, colorful, terminal-first Python environment manager.

`mew` is designed to make Python and Conda environment management feel simple, fast, and human-friendly.

Instead of remembering complex commands, you can use clean commands like:

```bash
mew craft
mew open
mew show
mew remove
```

---

# ✨ Features

- 🐍 Python venv support
- 🧪 Conda environment support
- 🎨 Colorful modern terminal UI
- ⚡ Interactive environment selector
- 🔒 Lock / unlock environments
- 🧬 Clone environments
- 🆔 Unique environment IDs
- 🧠 Name + ID resolution system
- 📦 Registry-based environment tracking
- 🖥 Automatic shell detection
- 🚀 Works with PowerShell, CMD, Bash

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/mew.git
cd mew
```

---

## 2. Install locally

```bash
pip install -e .
```

This installs `mew` globally in editable mode.

Now you can use:

```bash
mew
```

from anywhere in the terminal.

---

# 🚀 Commands

| Command | Purpose |
|---|---|
| `mew craft` | Create environment |
| `mew open` | Open / activate environment |
| `mew close` | Deactivate current environment |
| `mew show` | Show all environments |
| `mew about` | Show environment details |
| `mew remove` | Delete environment |
| `mew clone` | Clone environment |
| `mew sync` | Sync existing environments |
| `mew lock` | Protect environment |
| `mew unlock` | Remove protection |

---

# 🛠 Usage

## Create Environment

```bash
mew craft
```

Interactive flow:

- select backend
- select Python version
- enter environment name

---

## Show Environments

```bash
mew show
```

Displays:

- environment name
- unique ID
- backend
- Python version
- lock status

---

## Open Environment

```bash
mew open
```

Or directly:

```bash
mew open myenv
```

Or:

```bash
mew open 59a9c3
```

Supports:

- PowerShell
- CMD
- Bash
- Conda
- Python venv

---

## Close Environment

```bash
mew close
```

Quick deactivate helper for active environment.

---

## Remove Environment

```bash
mew remove
```

Protected environments cannot be removed until unlocked.

---

# 🔒 Environment Protection

Protect important environments from accidental deletion.

## Lock Environment

```bash
mew lock
```

## Unlock Environment

```bash
mew unlock
```

Locked environments display:

```txt
🔒 environment-name
```

---

# 🧬 Clone Environment

Clone existing environments quickly.

```bash
mew clone
```

Useful for:

- experiments
- testing
- backups
- temporary branches

---

# 🔄 Sync Existing Environments

Import already-created environments into `mew`.

```bash
mew sync
```

Supports:

- existing Conda envs
- existing venv environments

---

# 📁 Project Structure

```txt
mew/

├── mew/
│
├── commands/
├── core/
├── backends/
├── ui/
├── models/
├── data/
│
├── tests/
│
├── README.md
├── pyproject.toml
└── .gitignore
```

---

# 🧠 Environment Identity System

Each environment gets:

- readable name
- unique ID

Example:

```txt
teacher [backend]
api-env [8ee0d6]
```

This avoids collisions between environments with the same name.

---

# 🎨 UI Design

`mew` focuses heavily on:

- contrast colors
- smooth terminal UX
- interactive selectors
- clean layouts
- colorful status messages
- lightweight workflow

---

# ⚠ Notes

## Conda Environment Names

Conda does not allow:

- spaces
- `/`
- `#`
- `:`

`mew` automatically sanitizes invalid Conda names.

---

# 🔮 Planned Features

- shell integration
- snapshots
- environment export/import
- auto activation
- environment tags
- pinned environments
- plugin system
- package presets

---

# ❤️ Philosophy

Most environment managers feel:

- robotic
- verbose
- hard to remember

`mew` aims to feel:

- simple
- cute
- memorable
- fast
- beginner-friendly

while still being powerful.

---

# 📜 License

MIT License

