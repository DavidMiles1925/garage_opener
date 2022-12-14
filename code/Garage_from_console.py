import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)

mainloop = True

open_door = input("Open Garage?(y/n):")

while mainloop == True:

    if open_door in ["y"]:
        print("Moving Door")
        GPIO.output(11, GPIO.LOW)
        print("LOW")
        time.sleep(0.3)
        print("HIGH")
        GPIO.output(11, GPIO.HIGH)
        mainloop = False
    if open_door in ["n"]:
        mainloop = False

GPIO.cleanup()
print("cleanup")
exit()
