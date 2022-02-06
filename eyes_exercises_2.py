import pygame
import time

dis_width = 800
dis_height = 600
pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))

pygame.display.set_caption('Snake game for eKids')

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
light_blue = (96, 148, 188)

font_style = pygame.font.SysFont("comicsansms", 25)
messages = [
    "Рухайте очима зліва направо і навпаки",
    "Рухайте очима вверх потім вниз і навпаки",
    "По діагоналі з лівого верхнього кутка в правий нижній і навпаки",
    "По діагоналі з правого верхнього кутка в лівий нижній і навпаки",
    "Рухайте очима по годинниковій стрілці",
    "Рухайте очима проти годинникової стрілки",
    "Переводьте зір з ближнього об'єкту на дільній",
    "Міцно замружте очі"
]

pause = 5

def show_message_centered(msg, color):
    rendered_message = font_style.render(msg, True, color)
    text_rect = rendered_message.get_rect(center=(dis_width / 2, dis_height / 2))
    dis.blit(rendered_message, text_rect)

def show_message(pos_x, pos_y, msg, color):
    rendered_message = font_style.render(msg, True, color)
    dis.blit(rendered_message, [pos_x, pos_y])


for message in messages:
    for i in range(0, pause):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        dis.fill(light_blue)
        show_message_centered(message, white)
        show_message(400, 350, (i+1).__str__(), white)
        time.sleep(1)
        pygame.display.update()

pygame.quit()
quit()