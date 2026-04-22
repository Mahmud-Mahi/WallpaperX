# WallpaperX

WallpaperX is a smart wallpaper changer for XFCE that sets different wallpapers for each workspace and avoids repeating images until all have been used.

---

## ✨ Features

* 🧩 Different wallpaper for each workspace
* 🔁 No-repeat system (uses all images before repeating)
* 🖥️ Works with XFCE (`xfconf-query`)
* ⚡ Lightweight and fast
* 🤖 Supports automation with systemd

---

## 📸 Preview

Workspace--1
<img width="1920" height="1080" alt="preview1" src="https://github.com/user-attachments/assets/0006be92-67ee-48bb-807a-e23b282e5d50" />

Workspace--2
<img width="1920" height="1080" alt="Preview" src="https://github.com/user-attachments/assets/c258dbe7-9a14-410c-a2b7-c97c1ff12b74" />

Workspace--3
<img width="1920" height="1080" alt="demo" src="https://github.com/user-attachments/assets/8d018a86-5dc1-48b5-ace3-b7d15757fd2c" />

---

## 📦 Requirements

* Linux + XFCE
* `xfconf-query` and `xfdesktop`
* Python 3 (only for script version)

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Mahmud-Mahi/WallpaperX.git
cd WallpaperX
```

---

### 2. Run with sample wallpapers

```bash
python3 wallpaperx.py --dir ./Wallpapers
```

Or short:

```bash
python3 wallpaperx.py -d ./Wallpapers
```

Or, ⚡ Use the compiled file

```bash
chmod +x ./wallpaperx
./wallpaperx --dir ~/Pictures/Wallpapers
```

---

### 3. Use your own wallpapers

```bash
python3 wallpaperx.py --dir ~/Pictures/Wallpapers
```

Default folder (if not provided):

```text
~/Pictures/Wallpapers
```

---

## 🔄 Automation (Run Daily)

Create service:

```ini
~/.config/systemd/user/wallpaperx.service

[Unit]
Description=WallpaperX

[Service]
Type=oneshot
ExecStart=/path/to/wallpaperx --dir /path/to/wallpapers
Environment=DISPLAY=:0
Environment=XAUTHORITY=%h/.Xauthority
```

Create timer:

```ini
~/.config/systemd/user/wallpaperx.timer

[Timer]
OnCalendar=*-*-* 07:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable:

```bash
systemctl --user daemon-reload
systemctl --user enable --now wallpaperx.timer
```

---

## 🧠 How It Works

* Detects XFCE workspace wallpaper paths
* Picks unused images randomly
* Applies one wallpaper per workspace
* Stores history in `~/.cache/wallpaperx_history.txt`
* Resets automatically when all images are used

---

## 📁 Project Structure

```text
WallpaperX/
├── Wallpapers/
├── wallpaperx
├── wallpaperx.py
├── README.md
└── LICENSE
```

---

## ⚠️ Notes

* XFCE only
* Designed for laptop internal display (`monitoreDP`, `LVDS`, `DSI`)
* External monitors are ignored

---

## 🔮 Future Development

Planned improvements for WallpaperX:

* 🎯 Support for external monitors (multi-monitor setups)
* 🎨 Per-workspace themes (different categories of wallpapers)
* 🧠 Smarter selection modes (cycle, time-based, etc.)
* ⚙️ Command-line options for better control
* 🖥️ Simple GUI for easier usage
* 📦 Packaging as a `.deb` for easy installation

Contributions and ideas are welcome.

---

## 👤 Author

[Mahmud Mahi](mailto:mahmudurahmanmahi26@gmail.com)

---

## 📜 License

MIT License
