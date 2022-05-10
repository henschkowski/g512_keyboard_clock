import subprocess
import time
from datetime import datetime

while (True):
    NOW = datetime.now()

    min_tens = (int)(NOW.minute / 10)
    min_ones = NOW.minute % 10
    print("min_tens", min_tens)
    print("min_ones", min_ones)
    hour_ampm = 12 if NOW.hour == 12 else  NOW.hour % 12
    is_pm = True if (NOW.hour - 12 >= 0) else False
    print("hour_ampm", hour_ampm)
    print("is_pm",  is_pm)
    print("g810-led -p /etc/g810-led/profile")
    subprocess.run("g810-led -p /etc/g810-led/profile", shell=True)
    
    for keycode in [f"F{hour_ampm}", f"{min_tens}", f"num{min_ones}", "P", "A"]:
        color = "00ffff"
        if keycode == "A" and is_pm:
            color = "ff0000"
        if keycode == "P" and not is_pm:
            color = "ff0000"
        print(f"g810-led -k {keycode} {color}")
        subprocess.run(f"g810-led -k {keycode} {color}", shell=True)

    time.sleep(60)
