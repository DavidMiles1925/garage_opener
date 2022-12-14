import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)

print("Moving Door")
GPIO.output(11, GPIO.LOW)
print("LOW")
time.sleep(0.3)
print("HIGH")
GPIO.output(11, GPIO.HIGH)

GPIO.cleanup()
print("cleanup")
print("program stopped")
exit()