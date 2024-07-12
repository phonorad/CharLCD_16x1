import RPi.GPIO as GPIO
import time
import socket
import os

os.system('echo none | sudo tee /sys/class/leds/ACT/trigger')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(47,GPIO.OUT)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IPAddress: {ip_address}")
splitip = ip_address.split(".")
print(splitip)
intip = list(map(int, splitip))
print(str(intip))
GPIO.output(47,1)
time.sleep(5)
i = 0
while i < 4:
	ipnum = intip[i]
	for p, d in enumerate(str(abs(ipnum))):
		j = 0
		while j < int(d):
			time.sleep(0.5)
			GPIO.output(47,0)
			time.sleep(0.5)
			GPIO.output(47,1)
			j += 1
		time.sleep(1)
	time.sleep(1)
	GPIO.output(47,0)
	time.sleep(0.1)
	GPIO.output(47,1)
	time.sleep(1)
	i += 1
time.sleep(5)
os.system('echo actpwr | sudo tee /sys/class/leds/ACT/trigger')
