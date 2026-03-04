import network
import socket
import time

ssid = "ranjith"
password = "123456987"

# Connect WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Connected:", wifi.ifconfig())

# PC server IP
HOST = "192.168.1.100"
PORT = 5000

s = socket.socket()
s.connect((HOST, PORT))

while True:

    # Simulated camera data
    frame = "FRAME_READY"

    s.send(frame)

    print("Frame sent")

    time.sleep(2)