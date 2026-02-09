from machine import Pin
import network
import urequests
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)

led = machine.Pin("LED", machine.Pin.OUT)


where = "School"

if where == "School":
    ssid = "XTH_1-2972"
    password = "p{4615E4"
    SERVER_IP = "192.168.1.199"
else:
    ssid = "FWFamily"
    password = "Hdosfftvt2007!"
    SERVER_IP = "192.168.68.134"

URL = "http://" + SERVER_IP + ":5000/data"

# ---------- WiFi ----------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to WiFi...", end="")

timeout = 10
start = time.time()

while not wlan.isconnected():
    if time.time() - start > timeout:
        print("\nFailed to connect")
        raise RuntimeError("WiFi connection failed")
    time.sleep(0.5)
    print(".", end="")

print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])

# ---------- Data ----------
payload = {
    "device": "pico-w",
    "message": "MAN"
}

was_pressed = False

while True:
    if button.value() == 0 and not was_pressed:
        was_pressed = True
        print("Button pressed")

        try:
            response = urequests.post(URL, json=payload)
            print("Status:", response.status_code)
            print(response.text)
            
            if "LED" in response.text
                led.value(response.text["LED"])
            
            response.close()
        except Exception as e:
            print("POST failed:", e)

    elif button.value() == 1 and was_pressed:
        was_pressed = False 

    time.sleep(0.1)

