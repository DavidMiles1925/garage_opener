import RPi.GPIO as GPIO
import time
import pygame
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)

mainloop = True

#Graphic Coordinates
x = 400
y = 400
y2 = 0

#Intialize Pygame
pygame.init()

os.environ["DISPLAY"] = ":0"
pygame.display.init()
#Set up Pygame Window
window = pygame.display.set_mode((x,y))
pygame.display.set_caption("Garage")
#Create Font Surface
display_surface = pygame.display.set_mode((x,y))
white = (255, 255, 255)
fontname = pygame.font.get_default_font()
font = pygame.font.Font(fontname,12)
#Define output messages
text = font.render("Press ENTER to open door, ESC to QUIT", True, white, None)
moving_message = font.render("Door Moving", True, white, None)
exit_message = font.render("Terminating...", True, white, None)
invalid_message = font.render("Invalid Input", True, white, None)
#Instructions to user
display_surface.blit(text,(0,0))
pygame.display.update()

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                y2 = y2 + 12
                display_surface.blit(moving_message,(0,y2))
                pygame.display.update()
                print("Moving Door")
                GPIO.output(11, GPIO.LOW)
                print("LOW")
                time.sleep(0.3)
                print("HIGH")
                GPIO.output(11, GPIO.HIGH)
                
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            if event.key != pygame.K_ESCAPE and event.key != pygame.K_RETURN:
                y2 = y2 + 12
                display_surface.blit(invalid_message,(0,y2))
                pygame.display.update()

y2 = y2 + 12
display_surface.blit(exit_message,(0,y2))
pygame.display.update()
time.sleep(1)
print("terminate pygame")
pygame.quit()
GPIO.cleanup()
print("cleanup")
exit()
