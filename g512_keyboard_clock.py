import subprocess
import time
from datetime import datetime

min_ones_old = 0
interval=10
keyboard_found = True
while (True):
    time.sleep(interval)
    NOW = datetime.now()

    min_tens = (int)(NOW.minute / 10)
    min_ones = NOW.minute % 10
    hour_ampm = 12 if NOW.hour == 12 else  NOW.hour % 12
    is_pm = True if (NOW.hour - 12 >= 0) else False
    if min_ones == min_ones_old:
        time.sleep(interval)
        continue

    cp = subprocess.run("g810-led --list-keyboards", shell=True, capture_output=True)
    if "Matching or compatible device not found" in cp.stdout.decode("utf8"):
        if keyboard_found:
            keyboard_found = False
            print("No keyboard found")
        continue
    if not keyboard_found:
        print("Found a keyboard")
        keyboard_found = True

    # Reset colors
    subprocess.run("g810-led -p /etc/g810-led/profile", shell=True)

    for keycode in [f"F{hour_ampm}", f"{min_tens}", f"num{min_ones}", "P", "A"]:
        color = "00ffff"
        if keycode == "A" and is_pm:
            color = "ff0000"
        if keycode == "P" and not is_pm:
            color = "ff0000"
        subprocess.run(f"g810-led -k {keycode} {color}", shell=True)
    min_ones_old = min_ones
