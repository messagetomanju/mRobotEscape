import pygame

pygame.init()

screen_width = 600
screen_height = 600

#create screen
# size argument in set_mode requires tuple - it is immutable - changed, modified
#clock = pygame.time.Clock()

#create screen
# size argument in set_mode requires tuple - it is immutable - changed, modified
screen = pygame.display.set_mode((screen_width, screen_height))

robot_image = pygame.image.load("robo_image.png")
IMAGE_SIZE = (30, 30)
robot_image = pygame.transform.scale(robot_image,IMAGE_SIZE)
robot_x = 5
robot_y = 5


# infinite loop
run = True
while run:
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot_x -= 1
    if keys[pygame.K_RIGHT]:
        robot_x += 1
    if keys[pygame.K_UP]:
        robot_y -= 1
    if keys[pygame.K_DOWN]:
        robot_y += 1

    screen.fill((0,0,0))
    screen.blit(robot_image, (robot_x,robot_y))
    #screen.blit(robot_image, (40, 50))
    pygame.display.update()

pygame.quit()