import keyboard, pygame

pygame.init()
# screen = pygame.display.set_mode((500, 700))

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)

joystick.init()

done = False

deadzone = 0.2

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value >  0 + deadzone:
                        keyboard.write("d")
                    if event.value <  0 - deadzone:
                        keyboard.write("a")
                if event.axis == 1:
                    if event.value >  0 + deadzone:
                        keyboard.write("s")
                    if event.value <  0 - deadzone:
                        keyboard.write("w")


            # print(event)




#JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
