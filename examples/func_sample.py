import pygame

dis_width = 400
dis_height = 300
pygame.init()
dis = pygame.display.set_mode(size = (400, 300))

pygame.display.set_caption('Snake game for eKids')

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)

font_style = pygame.font.SysFont(None, 50)


def show_message(pos_x, pos_y, msg, color):
    rendered_message = font_style.render(msg, True, color)
    dis.blit(rendered_message, [pos_x, pos_y])


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    # pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    show_message(100, 100, "Sample text", blue)
    show_message(100, 200, "Sample text", red)
    show_message(150, 150, "Привіт", (0, 255, 0))
    pygame.display.update()

pygame.quit()
quit()