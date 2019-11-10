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
oldBus = " "
busCounter = 0

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value >  0 + deadzone:
                        bus = "d"
                    if event.value <  0 - deadzone:
                        bus = "a"
                if event.axis == 1:
                    if event.value >  0 + deadzone:
                        bus = "s"
                    if event.value <  0 - deadzone:
                        bus = "w"

        if bus == oldBus:
            busCounter += 1
            if busCounter == 10000:
                if busCounter % 5000 == 0:
                    keyboard.press(bus)

        if bus != "" and bus != oldBus:
            busCounter = 0
            keyboard.press(bus)
            oldBus = bus

        print(busCounter)

            # print(event)




#JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
