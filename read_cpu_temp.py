import time

treshold = 70
poll = 5
zone = "/sys/class/thermal/thermal_zone0/temp"

def read_temp():
    with open(zone) as f:
        return int(f.read().strip())/1000.0

while True:
    t = read_temp()
    if t > treshold:
        print(f"HOT:{t:.1f} *C")
    else:
        print(f"OK: {t:.1f} *C")
    time.sleep(poll)