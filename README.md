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

*Add a screenshot here showing different wallpapers on workspaces*

---

## 📦 Requirements

* Linux + XFCE
* `xfconf-query` and `xfdesktop`
* Python 3 (only for script version)

---

## 🚀 Quick Start

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

## ⚡ Use the Executable

```bash
chmod +x ./wallpaperx
./wallpaperx --dir ~/Pictures/Wallpapers
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

## 📜 License

MIT License

---

## 👤 Author

Mahmud Mahi
