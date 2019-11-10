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
    sleep(0.1)
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
                    print("0 dead")
                    if bus == "d" and deadA == False:
                        bus = "a"
                        deadA = True
                    if bus == "a" and deadA == False:
                        bus = "d"
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
                    print("1 dead")
                    if bus == "w" and deadB == False:
                        bus = "s"
                        deadB = True
                    if bus == "s" and deadB == False:
                        bus = "w"
                        deadB = True


    if bus != "":
        print(bus, deadA, deadB)
        keyboard.press(bus)



    if deadA == True and deadB == True:
        print("nah", event.value)
        bus = ""








#JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
