import requests
import time
import uuid

DEVICE_ID = str(uuid.uuid4())

SERVER_URL = "http://YOUR_KALI_IP:5000/track"

OLD_SIM = "Airtel"

def get_sim_info():
    return "Airtel"   # change to test

def get_location():
    return 17.3850, 78.4867

def send_data(sim_changed):
    lat, lon = get_location()

    data = {
        "device_id": DEVICE_ID,
        "latitude": lat,
        "longitude": lon,
        "sim_changed": sim_changed
    }

    try:
        res = requests.post(SERVER_URL, json=data)
        print("[+] Sent:", res.json())
    except:
        print("[-] Server not reachable")

while True:
    current_sim = get_sim_info()

    if current_sim != OLD_SIM:
        print("[🚨] SIM CHANGED")
        send_data(True)
        break
    else:
        print("[+] Normal")
        send_data(False)

    time.sleep(10)
