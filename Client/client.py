import network
import urequests
import json
import time

ssid = "XTH_1-2972"
password = "p{4615E4"

SERVER_IP = "192.168.1.199"  # <-- change this
URL = "http://" + SERVER_IP + ":5000/data"


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to WiFi...", end="")

timeout = 10  # seconds
start = time.time()

while not wlan.isconnected():
    if time.time() - start > timeout:
        print("\nFailed to connect")
        break
    time.sleep(0.5)
    print(".", end="")

if wlan.isconnected():
    print("\nConnected!")
    print("IP address:", wlan.ifconfig()[0])
    
    
# ---------- Send data ----------
payload = {
    "device": "pico-w",
    "uptime": time.ticks_ms()
}

headers = {"Content-Type": "application/json"}
for i in range(7):
    response = urequests.post(
        URL,
        data=json.dumps(payload),
        headers=headers
    )

    print("Status:", response.status_code)
    print(response.text)
    time.sleep(1)

response.close()
