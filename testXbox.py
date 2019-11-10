import pygame


pygame.init()
# screen = pygame.display.set_mode((500, 700))

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)

joystick.init()

done = False

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            print(event.type)
