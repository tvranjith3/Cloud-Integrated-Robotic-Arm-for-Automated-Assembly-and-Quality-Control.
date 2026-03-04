from machine import UART
import time

uart = UART(2, baudrate=9600, tx=17, rx=16)

while True:

    uart.write("FRAME_READY\n")

    if uart.any():
        msg = uart.readline()
        print(msg)

    time.sleep(1)