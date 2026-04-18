import argparse
import random
import subprocess
import sys
from pathlib import Path

DEFAULT_DIR = Path("~/Pictures/Wallpapers").expanduser()
HISTORY_PATH = Path("~/.cache/wallpaperx_history.txt").expanduser()
VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
LAPTOP_MONITOR_HINTS = ("monitoredp", "monitorlvds", "monitordsi")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Rotate XFCE wallpapers across monitors/workspaces."
    )
    parser.add_argument(
        "-d",
        "--dir",
        dest="dir_path",
        default=str(DEFAULT_DIR),
        help=f"Wallpaper directory path (default: {DEFAULT_DIR})",
    )
    return parser.parse_args()


def get_images(directory):
    return sorted(
        entry.name
        for entry in directory.iterdir()
        if entry.is_file() and entry.suffix.lower() in VALID_EXTENSIONS
    )


def load_history(history_file):
    if history_file.exists():
        return history_file.read_text(encoding="utf-8").splitlines()
    return []


def save_history(history_file, history):
    history_file.parent.mkdir(parents=True, exist_ok=True)
    history_file.write_text("\n".join(history), encoding="utf-8")


def get_wallpaper_properties():
    try:
        result = subprocess.run(
            ["xfconf-query", "-c", "xfce4-desktop", "-l"],
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError:
        print("Error: 'xfconf-query' was not found. This script requires XFCE.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        print(f"Error while reading XFCE wallpaper properties: {exc}", file=sys.stderr)
        sys.exit(1)

    all_properties = sorted(
        line.strip()
        for line in result.stdout.splitlines()
        if "workspace" in line and "last-image" in line and "backdrop" in line
    )
    for hint in LAPTOP_MONITOR_HINTS:
        matched_properties = [path for path in all_properties if hint in path.lower()]
        if matched_properties:
            return matched_properties

    print(
        "Error: no built-in laptop display was detected in XFCE wallpaper properties.",
        file=sys.stderr,
    )
    print(
        "Tip: expected a monitor name like eDP, LVDS, or DSI.",
        file=sys.stderr,
    )
    sys.exit(1)


def main():
    args = parse_args()
    dir_path = Path(args.dir_path).expanduser().resolve()

    if not dir_path.exists() or not dir_path.is_dir():
        print(f"Error: wallpaper directory does not exist: {dir_path}", file=sys.stderr)
        sys.exit(1)

    images = get_images(dir_path)
    if not images:
        print(f"No supported images found in: {dir_path}", file=sys.stderr)
        sys.exit(1)

    history = load_history(HISTORY_PATH)
    unused = [img for img in images if img not in history]

    wallpaper_properties = get_wallpaper_properties()
    if not wallpaper_properties:
        print(
            "Error: no XFCE wallpaper properties were detected. Make sure xfdesktop is managing the desktop.",
            file=sys.stderr,
        )
        sys.exit(1)

    slot_count = len(wallpaper_properties)
    if len(unused) < slot_count:
        print("Not enough unused images remain. Resetting history.")
        history = []
        unused = images[:]

    random.shuffle(unused)
    selected_images = unused[:slot_count]

    for property_path, image_name in zip(wallpaper_properties, selected_images):
        image_path = dir_path / image_name
        subprocess.run(
            [
                "xfconf-query",
                "--channel",
                "xfce4-desktop",
                "--property",
                property_path,
                "--set",
                str(image_path),
            ],
            check=True,
        )
        print(f"{property_path} -> {image_path}")

        if image_name not in history:
            history.append(image_name)

    save_history(HISTORY_PATH, history)
    subprocess.run(["xfdesktop", "--reload"], check=False)


if __name__ == "__main__":
    main()
