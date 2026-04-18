# WallpaperX

WallpaperX is a XFCE wallpaper rotator for laptop users. It changes the wallpapers of your laptop display workspaces, avoids repeats until the image pool is exhausted, and lets users choose the wallpaper folder from the command line instead of editing the script.

This project includes:

- the Python source file `wallpaperx.py`
- a compiled executable named `wallpaperx`
- a sample wallpaper folder named `Wallpapers/`

## Features

- Rotates wallpapers for XFCE workspaces on the built-in laptop display
- Prefers `monitoreDP`, then falls back to `monitorLVDS` or `monitorDSI`
- Accepts wallpaper directory from the command line with `--dir`
- Avoids repeating images until all available images have been used
- Saves wallpaper history in `~/.cache/wallpaperx_history.txt`
- Works well with `systemd --user` timers

## How It Works

WallpaperX asks XFCE for the available wallpaper property paths using `xfconf-query`.

It then:

- finds the workspace wallpaper paths for the laptop display
- reads images from the directory you provide
- skips images already used in previous runs
- resets the history automatically when all images have been used
- assigns one image per workspace
- reloads `xfdesktop` so the change appears immediately

## Requirements

- Linux with XFCE desktop
- `xfconf-query`
- `xfdesktop`
- Python 3

## Before You Run It

Make sure these are already set up on the user's system:

- XFCE is managing the desktop background
- the laptop display appears in XFCE wallpaper settings as `monitoreDP`, `monitorLVDS`, or `monitorDSI`
- the workspaces already exist in XFCE
- the wallpaper directory contains supported image files

Supported image formats:

- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.webp`

## Usage

Clone the project and run it with a wallpaper directory:

```bash
git clone https://github.com/Mahmud-Mahi/wallpaperx.git
cd wallpaperx
python3 wallpaperx.py --dir ~/Pictures/Wallpapers
```

If you want to use the included sample wallpaper folder:

```bash
python3 wallpaperx.py --dir ./Wallpapers
```

Short form:

```bash
python3 wallpaperx.py -d ./Wallpapers
```

If `--dir` is not provided, WallpaperX uses:

```text
~/Pictures/Wallpapers
```

## Compiled Executable

If you do not want to run the Python file directly, you can use the compiled executable included in the project:

```bash
chmod +x ./wallpaperx
./wallpaperx --dir ./Wallpapers
```

You can also point it to any other wallpaper folder:

```bash
./wallpaperx --dir ~/Pictures/Wallpapers
```

## Monitor Selection

WallpaperX is intentionally focused on the laptop's built-in display.

The script checks monitor names in this order:

1. `monitoreDP`
2. `monitorLVDS`
3. `monitorDSI`

As soon as one match is found, that monitor's workspace wallpaper paths are used. External displays are ignored.

## Example Output

```text
/backdrop/screen0/monitoreDP/workspace0/last-image -> /home/user/Pictures/Wallpapers/a.jpg
/backdrop/screen0/monitoreDP/workspace1/last-image -> /home/user/Pictures/Wallpapers/b.jpg
/backdrop/screen0/monitoreDP/workspace2/last-image -> /home/user/Pictures/Wallpapers/c.jpg
```

## Automation With systemd

You can run WallpaperX automatically with a user timer.

Create `~/.config/systemd/user/wallpaperx.service`:

```ini
[Unit]
Description=WallpaperX

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /path/to/wallpaperx.py --dir /path/to/wallpapers
Environment=DISPLAY=:0
Environment=XAUTHORITY=%h/.Xauthority
```

If you want to use the compiled executable instead, use:

```ini
[Unit]
Description=WallpaperX

[Service]
Type=oneshot
ExecStart=/path/to/wallpaperx --dir /path/to/wallpapers
Environment=DISPLAY=:0
Environment=XAUTHORITY=%h/.Xauthority
```

Create `~/.config/systemd/user/wallpaperx.timer`:

```ini
[Unit]
Description=Run WallpaperX daily

[Timer]
OnCalendar=*-*-* 07:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable it:

```bash
systemctl --user daemon-reload
systemctl --user enable --now wallpaperx.timer
```

## Project Files

```text
wallpaperx/
├── Wallpapers/
├── wallpaperx
├── wallpaperx.py
├── README.md
└── LICENSE
```

## Notes

- This project targets XFCE only
- This version is designed for laptop internal displays, not full multi-monitor wallpaper rotation
- Wallpaper history is shared across runs through `~/.cache/wallpaperx_history.txt`

## License

MIT License

## Author

Mahmud Mahi  
Email: [mahmudurahmanmahi26@gmail.com](mailto:mahmudurahmanmahi26@gmail.com)
