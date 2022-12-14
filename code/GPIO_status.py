import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

G11 = GPIO.input(11)
G13 = GPIO.input(13)
G15 = GPIO.input(15)

print("11:",G11)
print("13:",G13)
print("15:",G15)

exit()