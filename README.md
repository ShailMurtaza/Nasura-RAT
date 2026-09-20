# Nasura RAT

**Nasura** is a Python learning project that explores how remote administration tools work. It is built around sockets and demonstrates client–server communication, multi-client handling, and common remote-management features.

> **Educational use only.** Run this only on machines and networks you own or have explicit permission to administer. Unauthorized access to systems is illegal.

Created by **Shail Murtaza**.

---

## Project layout

| Variant | Description |
| --- | --- |
| **Nasura RAT (CLI) (SINGLE FILE)** | Single-file command-line server and client |
| **Nasura RAT (GUI)** | Web-based control panel (Bottle) with a browser UI |

Each variant includes:

- **Plain Text** — traffic sent without encryption (easier to study)
- **Encryption** — encrypted client/server communication for learning crypto in transit

---

## Core ideas

- **Python sockets** for reverse connections from client to server
- **`recvall()` / `sendall()`** helpers so transfers are not limited by a single `recv()` call (large payloads supported via a length header)
- **Multi-client management** — list, select (`use`), and disconnect clients by index
- **Client generation** — create a client script aimed at a chosen host and port

---

## Features

### Connection & session control

- Start a listener on a host/port
- List connected clients and select one by index
- Disconnect a client
- Create client payloads (plain or encrypted in the GUI)

### Remote shell

- Interactive command execution on the selected client (cross-platform reverse shell)

### File transfer & file manager

- Upload / download individual files
- Upload / download directories
- GUI file manager with drive listing and browse/upload/download

### Screen & capture

- Take screenshots from the client
- GUI screen share (live screenshot stream in the browser)

### System utilities (GUI “Extra” + related commands)

- Shutdown / restart / log off (with optional delay)
- Task list and process kill
- Run as administrator (Windows)
- Dump saved Wi‑Fi credentials (Windows, for learning local credential storage)
- Attach client to Windows Startup (persistence demo)

### CLI extras

- Command-line argument support on the single-file variant
- Built-in `help` and `servery.help` command reference

---

## GUI modules (browser)

When a client is selected, the web UI exposes:

| Module | Purpose |
| --- | --- |
| **Home** | Start listener / create client |
| **Clients** | View and manage connections |
| **CMD** | Remote shell |
| **Screenshot** | Capture and view screenshots |
| **Attach Startup** | Windows Startup persistence demo |
| **File Manager** | Browse, upload, and download files |
| **Screen Share** | Live screen view |
| **Extra** | Power controls, tasks, Wi‑Fi dump, elevation |

---

## Tech stack

### Language & runtime

| Technology | Role |
| --- | --- |
| **Python** | Main language for server, client, protocol, and GUI backend |
| **Python `socket`** | TCP client–server transport (reverse connections) |
| **`threading`** | Background listener thread so the CLI/GUI stays responsive while accepting clients |
| **`subprocess`** | Runs shell commands on the remote client |
| **`shutil`** | Directory zip/archive for folder upload/download; file copy for startup attach |
| **`marshal`** | Serialize/compile client payload code when generating encrypted clients |
| **`ctypes`** | Windows API helpers (e.g. elevation / admin-related demos) |
| **`os` / `sys` / `time` / `datetime`** | Paths, process control, delays, and timestamps |

### Third-party Python libraries

| Library | Role |
| --- | --- |
| **[Bottle](https://bottlepy.org/)** | Lightweight WSGI web framework for the GUI control panel (routes, templates, forms, static files) |
| **[cryptography](https://cryptography.io/)** (`Fernet`) | Symmetric encryption for the Encryption variants (key generation + encrypt/decrypt of traffic or client payloads) |
| **[PyAutoGUI](https://pyautogui.readthedocs.io/)** | Client-side screenshots (`screenshot`) used for capture and screen share |
| **[win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)** | Windows desktop toast notifications when events happen in the GUI server |
| **[PyInstaller](https://www.pyinstaller.org/)** | Optional packaging of client scripts into standalone `.exe` (`zcreate_exe.py`) |

### GUI front end

| Technology | Role |
| --- | --- |
| **HTML** | Bottle templates for Home, Clients, Shell, File Manager, Screenshot, Screen Share, Extra |
| **CSS** | Custom styles (`main.css`, `navbar.css`, `tooltip.css`) plus **W3.CSS** for layout/components |
| **JavaScript** | Small UI helpers (e.g. message dismiss, table toggles, delete checks) |

### Architecture summary

```
Browser (HTML/CSS/JS)
        │  HTTP
        ▼
Bottle web app (Nasura.py / web.py)
        │  Python sockets (+ optional Fernet)
        ▼
Remote client (socket + PyAutoGUI + subprocess + OS APIs)
```

- **CLI variant** skips Bottle and the browser; you drive the same socket protocol from the terminal.
- **Plain Text** uses raw socket bytes; **Encryption** wraps sensitive data with Fernet.

---

## Learning goals

This repo is useful for practicing:

1. Socket programming and framing (headers + streaming)
2. Multi-client reverse-connection architecture
3. Building a small web front end over a socket backend
4. Contrast between plaintext and encrypted remote protocols
5. How remote-admin features map to OS APIs (shell, files, screen, power)

---

## Versions noted in tree

- GUI: **Nasura Rat GUI VERSION 5.2**
- CLI: **Python Socket Reverse Shell Version 5**

For command syntax on the CLI build, see `Nasura RAT (CLI) (SINGLE FILE)/README.md` and the `servery.help` files under each variant.
