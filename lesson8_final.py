import pygame
import time
import random
# Імпортуємо картинки фруктів
from assets import fruits
# Імпортуємо картинки змійки - голови і тіла
from assets import snake_imgs

# Кольори
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
light_blue = (96, 148, 188)
red = (213, 50, 80)
orange = (255, 165, 48)
violet = (117, 48, 255)

# Розміри екрану і ініціалізація екрану
dis_width = 800
dis_height = 600
pygame.init()
dis = pygame.display.set_mode(size=(dis_width, dis_height))  # Змінна dis - для роботи з екраном, виводу графіки
pygame.display.set_caption("Snake game for EKIDS2021")  # Заголовок вікна
icon = pygame.image.load('assets/img/head.png')  # Готуємо іконку
pygame.display.set_icon(icon)  # Встановлюємо віконку

# Настройки гри - розмір блоку змійки/фрукта, початкова швидкість, приріст швидкості, кількість рівнів, кількість фруктів на рівень
snake_block = 20
initial_snake_speed = 5
levels = 5
level_speed_add = 3
fruits_per_level = 5

# Змінна годинника, для швидкості і затримок
clock = pygame.time.Clock()

# Шрифти для текстових написів
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Фонове зображеня
background_img = pygame.image.load("assets/img/sand1.jpg")

# Звуки
apple_sound = pygame.mixer.Sound('assets/sound/apple.wav')
explosion_sound = pygame.mixer.Sound('assets/sound/explosion.wav')
game_over_sound = pygame.mixer.Sound('assets/sound/gameover.wav')
level_up_sound = pygame.mixer.Sound('assets/sound/level_up.mp3')


def your_score(score):
    # Метод для виводу рахунку на екран під час гри
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [25, 25])


def your_level(value):
    # Метод для виводу рівня під час гри
    value = score_font.render("Your Level: " + str(value), True, yellow)
    dis.blit(value, [25, 100])


def draw_our_snake(snake_list, level):
    # метод для виводу зображень змійки на екран, використовуються зображення із assets/snake_imgs
    for x in snake_list[0:-1]:
        # кожна частинка змійки крім голови
        dis.blit(snake_imgs.bodies[level - 1], (x[0], x[1]))
    # виводимо голову
    dis.blit(snake_imgs.heads[level - 1], (snake_list[-1][0], snake_list[-1][1]))


def message(msg, color, pos_x=dis_width / 6, pos_y=dis_height / 3):
    # універсальний метод виводу повідомлень на заставках
    rendered_message = font_style.render(msg, True, color)
    dis.blit(rendered_message, [pos_x, pos_y])


def starting_screen():
    # Початковий екран гри
    while True:
        for i in range(-10, 1):  # десять
            dis.fill(orange)
            message("Game will start in: " + str(i * (-1)) + " or press r to run the game", violet)
            message("Select speed on Snake: * 1 - slow mode * 2 - medium mode * 3 - fast mode", violet,
                    pos_y=dis_height / 2)
            pygame.display.update()
            time.sleep(1)  # по одній секунді
            # Після виводу повідомлень чекаємо 10 секунд (10*1), перевіряємо натискання клавіш вибору швидкості і починаємо гру
            if i == 0:
                gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameLoop()
                    elif event.key == pygame.K_1:
                        gameLoop(snake_speed=7)
                    elif event.key == pygame.K_2:
                        gameLoop(snake_speed=20)
                    elif event.key == pygame.K_3:
                        gameLoop(snake_speed=30)


def gameLoop(snake_speed=initial_snake_speed):
    # Гра. Основний метод з початковими значеннями самої гри і основним циклом
    game_over = False
    game_win = False
    game_close = False
    fruit_eaten = False
    current_fruit = 0
    bad_fruit = 0

    # Початкові положення змійки - середина екрану
    x1 = dis_width / 2
    y1 = dis_height / 2
    # Початковий напрямок руху змійки - 0
    x1_change = 0
    y1_change = 0

    # Ініціалізуємо змійку
    snake_list = []  # Масив, в якому зберігаються пари координат блоків змійки
    length_of_snake = 1  # Початкова дожвина
    level = 1  # Початковий рівень

    # Генеруємо координати корисного фрукта
    food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    # Генеруємо координати поганого фрукта
    bad_food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    bad_food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_close:  # Головний цикл, працює, поки не буде встановлено game_close в True

        while game_over == True or game_win == True:
            # якщо виграли чи програли виводимо повідомлення і очікуємо дію - почати знову або закрити програму
            if game_over:
                message("You Lost! Press C-Play Again or Q-Quit", red)
            else:
                dis.fill(orange)
                message("You Win! Press C-Play Again or Q-Quit", black)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                        exit()  # вихід
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                # перевірка вводу користувача. якщо натиснута клавіша, перевірити, чи це не стрілочка.
                # якщо стрілочка - задати швидкість руху змійки і відповідному напрямку
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # блок для переміщення змійки через границю екрану, рух продовжується з протилежного боку.
        if x1 >= dis_width:
            x1 = 0
        if x1 < 0:
            x1 = dis_width
        if y1 >= dis_height:
            y1 = 0
        if y1 < 0:
            y1 = dis_height

        # обраховуємо нове положення змійки, в кожному кроці гри.
        x1 += x1_change
        y1 += y1_change

        # Виводимо фон
        dis.blit(background_img, [0, 0])
        # Виводимо корисний фрукт - з масиву фруктів
        dis.blit(fruits.good[current_fruit], (food_x, food_y))

        # Виводимо поганий фрукт - з масиву поганих фруктів
        dis.blit(fruits.bad[bad_fruit], (bad_food_x, bad_food_y))

        # Cтворюємо нову позицію змійки - для голови
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)  # Додаємо ному позицію до масиву змійки
        if len(snake_list) > length_of_snake:  # забираємо останню позицію з масиву змійки - змійка перемістилась
            del snake_list[0]

        for x in snake_list[:-1]:  # перевіряємо, чи змійка не вкусила сама себе, для кожної з координат тіла
            if x == snake_head:  # якщо коордитната тіла рівна голові - вкусила
                game_over_sound.play()
                game_over = True  # і гра закінчується

        draw_our_snake(snake_list, level)  # виводимо змійку
        your_score(len(snake_list) - 1)  # виводимо рахунок
        your_level(level)  # виводимо рівень

        pygame.display.update()  # оновлюємо екран

        if x1 == bad_food_x and y1 == bad_food_y:  # перевіряємо, чи змійка з'їла поганий фрукт, координати голови рівні координатам поганого фрукта
            print("Fooo!!")
            explosion_sound.play()
            length_of_snake -= 1  # мінусуємо довжину
            snake_list.pop(0)  # мінусуємо довжину
            fruit_eaten = True  # запам'ятовуємо, що змійка щось з'їла, щоб згенерувати нові фрукти

        if x1 == food_x and y1 == food_y:  # перевіряємо, чи змійка з'їла хороший фрукт, координати голови рівні координатам поганого фрукта
            print("Yummy!!")
            apple_sound.play()
            length_of_snake += 1  # збільшуємо довжину
            fruit_eaten = True  # запам'ятовуємо, що змійка щось з'їла, щоб згенерувати нові фрукти

        if fruit_eaten:  # якщо змійка щось з'їла на цьому кроці - генеруємо нові фрукти
            fruit_eaten = False
            current_fruit = random.randrange(0, len(fruits.good))  # випадковий хороший фрукт з масиву хороших
            food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

            bad_fruit = random.randrange(0, len(fruits.bad))  # випадковий поганий фрукт з відповідного масиву
            bad_food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            bad_food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

            if length_of_snake == 0:  # якщо довжина змійки 0 - гра закінчується, змійка переїла отруйних яблук
                game_over = True
            if length_of_snake % fruits_per_level == 0 and not game_over:
                # якщо довжина змійки кратка кількості фруктів на рівень - починаємо новий рівень
                level += 1
                if level == levels:  # якщо новий рівень рівний максимальному - перемогу
                    game_win = True
                else:
                    # інакше - збільшуємо швидкість, виводимо повідомлення про новий рівень
                    snake_speed += level_speed_add
                    dis.fill(light_blue)
                    message("Level passed!", violet)
                    pygame.display.update()
                    level_up_sound.play()
                    time.sleep(2)

        clock.tick(snake_speed)  # пауза для кожного кроку гри

    pygame.quit()  # вихід
    quit()


starting_screen()  # власне запуск - починаємо зі стартового екрану
