import os
import random
import subprocess

dir_path = "/home/mahmud_mahi/Pictures/Wallpapers"
history_path = os.path.expanduser("~/.cache/wallpaperx_history.txt")

# Get all images
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
images = [f for f in os.listdir(dir_path) if f.lower().endswith(valid_extensions)]

# Load history
if os.path.exists(history_path):
    with open(history_path, 'r') as f:
        history = f.read().splitlines()
else:
    history = []

# 3. Filter out used images
unused = [img for img in images if img not in history]

# 4. Get all monitor properties to see how many we need
result = subprocess.run(
    ["xfconf-query", "-c", "xfce4-desktop", "-l"],
    capture_output=True, text=True
)

monitor_paths = [line for line in result.stdout.splitlines() if "monitoreDP" in line and "workspace" in line and "last-image" in line]
num_monitors = len(monitor_paths)

# 5. If not enough unused images remain for all monitors, reset history
if len(unused) < num_monitors:
    print("Not enough unused images. Resetting history.")
    history = []
    unused = images

if not unused:
    print("No images found in directory!")
    exit(1)

# 6. Shuffle and select only what we need for today
random.shuffle(unused)
selected_today = unused[:num_monitors]

# Assign different wallpaper to each monitor
for i, monitor in enumerate(monitor_paths):
    img_name = selected_today[i]
    image_path = os.path.join(dir_path, img_name)
    
    subprocess.run([
        "xfconf-query",
        "--channel", "xfce4-desktop",
        "--property", monitor,
        "--set", image_path
    ])

    print(f"{monitor} → {image_path}")
    
    # Add to history
    if img_name not in history:
        history.append(img_name)

# 7. Save updated history
with open(history_path, 'w') as f:
    f.write('\n'.join(history))

# Reload XFCE desktop (ensures instant update)
subprocess.run(["xfdesktop", "--reload"])