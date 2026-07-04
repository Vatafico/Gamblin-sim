import pygame 

pygame.init()

screen = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Ground floor")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((200, 200, 200))

    pygame.display.flip()


pygame.quit