import keyboard, pygame
from time import sleep

pygame.init()
# screen = pygame.display.set_mode((500, 700))

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)

joystick.init()

done = False

deadzone = 0.2
bus = ""

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value >  0 + deadzone:
                        keyboard.press("d")
                        sleep(0.5)
                    if event.value <  0 - deadzone:
                        keyboard.press("a")
                        sleep(0.5)
                if event.axis == 1:
                    if event.value >  0 + deadzone:
                        keyboard.press("s")
                        sleep(0.5)
                    if event.value <  0 - deadzone:
                        keyboard.press("w")
                        sleep(0.5)



            # print(event)




#JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
