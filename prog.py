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

millis = 0
oldMillis = 0

oldVal = 0
val = 0

deadA = False
deadB = False

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value >  0 + deadzone or event.value < 0 - deadzone:
                        deadA = False
                        print("ye", event.value)
                        if event.value > 0:
                            bus = "d"
                        if event.value < 0:
                            bus = "a"
                    if event.value < 0 + deadzone and event.value > 0 - deadzone:
                        deadA = True

                if event.axis == 1:
                    if event.value >  0 + deadzone or event.value < 0 - deadzone:
                        deadB = False
                        print("ye", event.value)
                        if event.value > 0:
                            bus = "s"
                        if event.value < 0:
                            bus = "w"
                    if event.value < 0 + deadzone and event.value > 0 - deadzone:
                        deadB = True

                if deadA == True and deadB == True:
                    print("nah", event.value)
                    bus = ""




        print(bus)
        sleep(0.1)
        if bus != "":
            # print(bus)
            keyboard.press(bus)
        #
        #     millis = int(round(time.time() * 1000))
        #     keyboard.press(bus)

            # print(event)




#JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
