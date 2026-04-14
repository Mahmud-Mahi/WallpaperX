# wallpaperx

A smart wallpaper rotator for XFCE that automatically changes wallpapers across multiple workspaces and monitors without repeating images.

## ✨ Features

* 🖥️ Multi-monitor support (HDMI, eDP, VGA, etc.)
* 🧩 Per-workspace wallpaper control
* 🔁 No-repeat algorithm (cycles through all wallpapers before repeating)
* ⚡ Fast and lightweight
* 🛠️ Works with XFCE (`xfconf-query`)
* ⏱️ Automation support via systemd timers

---

## 📸 How It Works

* Detects all XFCE workspace wallpaper paths
* Selects unused wallpapers randomly
* Applies different wallpapers to each workspace
* Stores history to prevent repetition
* Resets automatically when all images are used

---

## 📦 Requirements

* XFCE Desktop Environment
* `xfconf-query`
* Python 3 (if running script directly)

---

## 🚀 Installation

### Option 1: Run Python script

```bash
git clone https://github.com/yourusername/wallpaperx.git
cd wallpaperx
python3 wallpaper.py
```

### Option 2: Use compiled binary (PyInstaller)
coming soon
```bash
chmod +x wallpaperx
./wallpaperx
```

---

## ⚙️ Configuration

Edit the script:

```python
dir_path = "/home/your-username/Pictures/Wallpapers"
```

---

## 🧠 Automation (systemd timer)

Create a user service and timer to run daily:

```ini
# ~/.config/systemd/user/wallpaper.service
[Unit]
Description=WallpaperX Service

[Service]
ExecStart=/path/to/wallpaperx
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/your-username/.Xauthority
```

```ini
# ~/.config/systemd/user/wallpaper.timer
[Timer]
OnCalendar=*-*-* 07:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable it:

```bash
systemctl --user daemon-reload
systemctl --user enable wallpaper.timer
systemctl --user start wallpaper.timer
```

---

## 📁 Project Structure

```
wallpaperx/
├── wallpaper.py
├── README.md
└── .gitignore
```

---

## 🔮 Future Improvements

* CLI options (random / cycle modes)
* Per-workspace themes
* GUI interface
* Packaging as `.deb`

---

## 🤝 Contributing

Pull requests are welcome. Feel free to suggest improvements or new features.

---

## 📜 License

MIT License

---

## 💡 Author

Mahmud Mahi -

