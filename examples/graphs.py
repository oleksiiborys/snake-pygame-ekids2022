import pygame

dis_width = 500
dis_height = 500
pygame.init()
dis = pygame.display.set_mode(size = (dis_width, dis_height))

pygame.display.set_caption('Snake game for eKids')

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
light_blue = (96, 148, 188)
red = (213, 50, 80)

def fun0(x):
    return x**1.5

def fun1(x):
    return x*x

def fun2(x):
    return x**0.5

def fun3(x):
    return 1/x

def fun4(x):
    return 10/x

def fun5(x):
    return x

def fun6(x):
    return 500-x


array = [
    [fun0, light_blue, 5],
    [fun1, yellow, 5],
    [fun2, red, 0.05],
    [fun3, blue, 5000],
    [fun4, white, 5000],
    [fun5, green, 1],
    [fun6, green, 1]
]
for func,color,scale in array:
    res = []
    for x in range(1,dis_width):
        y = func(x/scale)
        res.append((x,y))
        if (x > dis_height):
            break
    print(res)
    for i in range(1, len(res)):
        x,y = res[i]
        # prev_x,prev_y = res[i-1]
        pygame.draw.rect(dis, color, [x,dis_height - y, 1, 1])
        # pygame.draw.line(dis, color, [x,dis_height - y], [prev_x,dis_height - prev_y])


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
