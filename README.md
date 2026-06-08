<div align="center">
<p align="center">
	<img src="asset/mew_logo_trans.png" alt="mew" width="170" />
</p>

# **MEW** — Lightweight Python environment manager

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-purple)](#)
[![Conda](https://img.shields.io/badge/Conda-Supported-44A833?logo=anaconda&logoColor=white)](#)
[![venv](https://img.shields.io/badge/venv-Supported-green)](#)
[![CLI](https://img.shields.io/badge/interface-Terminal-orange)](#)
[![Status](https://img.shields.io/badge/status-Active%20Development-brightgreen)](#)
[![Made with Python](https://img.shields.io/badge/Made%20With-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

---

### **Craft • Activate • Clone • Lock • Repeat**

</div>


<p align="center">
	<img src="asset/mew_banner.png" alt="MEW" />
</p>

---

`mew` is a modern, terminal-first environment manager for Python and Conda designed to make environment workflows simple, fast, and predictable.

Built for developers who prefer working in the terminal, mew provides a clean interactive experience for creating, activating, cloning, protecting, and managing environments without the complexity of traditional tools. It combines a lightweight workflow with powerful features such as environment locking, cloning, syncing, unique environment IDs, and interactive environment selection.

mew supports both Python virtual environments (`venv`) and Conda environments through a unified interface, allowing you to manage multiple environment backends with the same commands and workflow. Whether you're working on personal projects, open-source contributions, research, or production applications, mew helps keep your development environments organized and easy to manage.

</div>

---

Table of Contents
-----------------

- [About](#about)
- [Showcase](#showcase)
- [Quick Start](#quick-start)
- [Features](#features)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## About

**mew** is a modern, terminal-first environment manager for Python and Conda that makes environment creation, activation, cloning, and management simple, fast, and predictable.

It provides a lightweight but powerful CLI for everyday environment workflows. Environments are tracked in a registry using human-friendly names and unique IDs, making them easy to find, manage, and activate.

mew supports both **Python virtual environments (`venv`)** and **Conda environments** through a unified interface, allowing developers to work with multiple environment backends without changing their workflow.

### Features

- 🐍 Python `venv` support
- 🧪 Conda environment support
- ⚡ Fast environment creation and activation
- 🎨 Interactive terminal UI
- 🆔 Human-friendly names with unique IDs
- 🔒 Environment locking and protection
- 🧬 Environment cloning
- 🔄 Environment synchronization
- 🎯 Open environments by name or ID
- 💻 PowerShell, CMD, and Bash support
- 🌎 Cross-platform workflow

### Philosophy

mew focuses on developer experience by making common environment tasks easy and consistent:

**Craft • Activate • Clone • Lock • Manage**

All from one beautiful terminal interface.


## Showcase

<p align="center">
	<img src="asset/mew_page.png" alt="mew UI demo" width="720" />
</p>


## Quick Start

Clone and install locally:

```bash
git clone https://github.com/A3x-parvez/mew.git
cd mew
pip install -e .
```

Run the interactive helper:

```bash
mew craft
```

## Features

- Support for Python `venv` and `Conda` environments
- Registry-backed environment tracking
- Interactive selectors and modern terminal UI
- Lock/unlock protection for important environments
- Clone, sync, and export workflows
- Portable, minimal, and scriptable CLI

## Commands

| Command | Description |
|---|---|
| `mew craft` | Create a new environment (interactive) |
| `mew open [NAME/ID]` | Activate or open an environment by name or ID |
| `mew close` | Deactivate current environment |
| `mew show` | List tracked environments |
| `mew about` | Show environment details |
| `mew remove` | Remove an environment (requires unlock) |
| `mew clone` | Clone an existing environment |
| `mew sync` | Import existing system environments into the registry |
| `mew lock` / `mew unlock` | Protect or unprotect an environment |

## Usage examples

Create an environment with the interactive flow:

```bash
mew craft
```

Open an environment by name or ID:

```bash
mew open myenv
mew open 59a9c3
```

List environments:

```bash
mew show
```

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/your-feature`.
3. Make changes and add tests where appropriate.
4. Open a pull request describing your changes.

Please keep changes focused and document new behaviors in the README or inline help.

## License

This project is licensed under the MIT License — see the included `LICENSE` file for details.

---

Maintainers: the project maintainers and community contributors.


## Header & Branding

The project header places the logo above a bold, prominent project name to create immediate recognition. The centered images above show the mark and an inline UI demo — perfect for landing pages and GitHub README viewers.

---

## Detailed Commands

Below are the primary commands with recommended usage patterns, flags, and examples to help new users get productive quickly.

- `mew craft`
	- Purpose: Guided environment creation flow.
	- Flow: select backend → choose Python version → name environment → optional packages
	- Example:

		```bash
		mew craft
		```

- `mew open [NAME|ID]`
	- Purpose: Activate or open an environment by friendly name or short ID.
	- Examples:

		```bash
		mew open myenv
		mew open 59a9c3
		```

- `mew close`
	- Purpose: Deactivate the current active environment (shell-friendly helper).
	- Example:

		```bash
		mew close
		```

- `mew show`
	- Purpose: List tracked environments with readable names, IDs, backend, Python version, and lock status.
	- Flags:
		- `--json` — output machine-readable JSON
		- `--all` — show system environments not yet in registry
	- Example:

		```bash
		mew show --json
		```

- `mew about [NAME|ID]`
	- Purpose: Show full metadata for an environment (path, packages, creation time, owner).
	- Example:

		```bash
		mew about myenv
		```

- `mew remove [NAME|ID]`
	- Purpose: Remove an environment tracked by `mew`.
	- Safety: Requires unlock for protected environments; supports `--yes` to skip confirmation.
	- Example:

		```bash
		mew remove myenv
		mew remove 59a9c3 --yes
		```

- `mew clone [SOURCE] [DEST]`
	- Purpose: Create a new environment by cloning an existing one.
	- Example:

		```bash
		mew clone myenv myenv-copy
		```

- `mew sync`
	- Purpose: Import system `venv` or `conda` environments into the `mew` registry.
	- Flags: `--auto` to import without prompts.

- `mew lock [NAME|ID]` / `mew unlock [NAME|ID]`
	- Purpose: Protect or unprotect environments from deletion.
	- Example:

		```bash
		mew lock important-env
		mew unlock important-env
		```

---

## Extended Feature List

- Environment identity system: human-friendly names + compact unique IDs for collision-free workflows.
- Portable registry: export/import the registry file for teams or CI.
- Interactive terminal UX: color, keyboard navigation, and clear affordances.
- Backend-agnostic workflows: `venv` and Conda parity for common tasks.
- Safety-first operations: locks and explicit confirmations to prevent data loss.

---

## Project Structure (high level)

```
mew/
│
├── mew/
│   │
│   ├── __main__.py
│   ├── cli.py
│   ├── config.py
│   ├── registry.py
│   │
│   ├── commands/
│   │   ├── craft.py
│   │   ├── open.py
│   │   ├── close.py
│   │   ├── show.py
│   │   ├── remove.py
│   │   └── about.py
│   │
│   ├── core/
│   │   ├── manager.py
│   │   ├── detector.py
│   │   ├── activator.py
│   │   ├── storage.py
│   │   ├── resolver.py
│   │   └── ids.py
│   │
│   ├── backends/
│   │   ├── venv.py
│   │   └── conda.py
│   │
│   ├── ui/
│   │   ├── select.py
│   │   ├── display.py
│   │   └── prompt.py
│   │
│   └── models/
│       └── environment.py
│
├── README.md
├── pyproject.toml
└── .gitignore

```

Each top-level component is intentionally small and focused so contributors can quickly find the code relevant to a feature.

---

## Installation & Local Development

Clone and install (editable):

```bash
git clone https://github.com/your-username/mew.git
cd mew
pip install -e .
```

Run the CLI locally:

```bash
mew
mew --help
```

## Tips for catching attention

- Keep the header visuals large and centered (done above).
- Lead with a short demo GIF or large screenshot to show the UX immediately.
- Provide copyable examples for each command (users can copy-paste).
- Offer `--json` or machine-readable outputs to encourage automation and CI adoption.

---

## Contributing

Contributions are welcome — please open issues or PRs. For code changes:

1. Fork the repo.
2. Create a feature branch.
3. Run tests and linters (if provided).
4. Open a PR with a concise description and example usage.

---

## **Author**

<div align="center">

### Built with ❤️ by Rijwanool Karim

Founder of **Wtero** • AI Engineer • Full-Stack Developer • Open Source Enthusiast

<p>
  <a href="https://github.com/A3x-parvez">
    <img src="https://img.shields.io/badge/GitHub-A3x--parvez-black?style=for-the-badge&logo=github" />
  </a>
  
  <a href="https://www.linkedin.com/in/rijwanool-karim">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin" />
  </a>

  <a href="https://rijwanool-karim.vercel.app/" target="_blank">
	<img src="https://img.shields.io/badge/Portfolio-Visit%20Website-8B5CF6?style=for-the-badge&logo=vercel&logoColor=white" />
	</a>
  
  <a href="https://wtero.com">
    <img src="https://img.shields.io/badge/Wtero-Official%20Website-8B5CF6?style=for-the-badge" />
  </a>
</p>


</div>

---

### Support the Project

If you find RagFlow useful:

- ⭐ Star the repository
- 🐛 Report bugs and suggest features
- 🔀 Submit pull requests
- 📢 Share the project with others

Your support helps improve the project and future open-source AI tools.


## **License**

Distributed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---



