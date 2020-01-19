import pygame
from random import randint, choice
from Snake import Snake
from Snake import Fruit
from Snake import Colors
from Snake import Dimensions
from Snake import Enemy
from math import inf, floor, sqrt

Out = False
pygame.init()
background = pygame.display.set_mode((Dimensions.WIDTH, Dimensions.HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()


def game_loop():
    snake = Snake(background, 100, 20)
    fruit = Fruit(background, randint(10, Dimensions.WIDTH - 10), randint(10, Dimensions.HEIGHT - 10))
    x = Dimensions.WIDTH * 0.45
    y = Dimensions.HEIGHT * 0.8
    speed = 2

    x_change = 0
    y_change = 0

    game_exit = False
    can_up = True
    can_down = True
    can_left = True
    can_right = True
    score = 0
    enemies = []

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if can_left:
                        x_change = -1 * speed
                        y_change = 0
                        can_left = False
                        can_right = False
                        can_up = True
                        can_down = True

                if event.key == pygame.K_RIGHT:
                    if can_right:
                        x_change = speed
                        y_change = 0
                        can_left = False
                        can_right = False
                        can_up = True
                        can_down = True

                if event.key == pygame.K_DOWN:
                    if can_down:
                        y_change = speed
                        x_change = 0
                        can_down = False
                        can_up = False
                        can_right = True
                        can_left = True

                if event.key == pygame.K_UP:
                    if can_up:
                        y_change = -1 * speed
                        x_change = 0
                        can_up = False
                        can_down = False
                        can_left = True
                        can_right = True

        x += x_change
        y += y_change
        if x < 0:
            x = Dimensions.WIDTH
        if y < 0:
            y = Dimensions.HEIGHT
        if x > Dimensions.WIDTH:
            x = 0
        if y > Dimensions.HEIGHT:
            y = 0

        background.fill(Colors.BLACK)
        snake = Snake(background, x, y)
        if Dimensions.d(snake.head_x, snake.head_y, fruit.x, fruit.y) < 4:
            fruit = Fruit(background, randint(0, Dimensions.WIDTH), randint(0, Dimensions.HEIGHT))
            score += 1
            if score // 5 > 0 and score % 5 == 0:
                speed = 1.2 * speed
                enemies.append(
                    Enemy(background, randint(10, Dimensions.WIDTH - 10), randint(10, Dimensions.HEIGHT - 10),
                          randint(0, 255), randint(0, 255), randint(0, 255)))
        else:
            fruit = Fruit(background, fruit.x, fruit.y)
        #for i in range(len(enemies)):
        i = 0
        while i < len(enemies):
            #x_final, y_final = find_shortest_path(enemies[i].x, enemies[i].y, x, y, speed*0.45)
            x_c = randint(-1,1) * int(speed)
            y_c = randint(-1, 1) * int(speed)
            #enemies[i] = Enemy(background, x_final, y_final, enemies[i].r, enemies[i].g, enemies[i].b)
            #enemies[i] = Enemy(background, enemies[i].x + x_c, enemies[i].y + y_c, enemies[i].r, enemies[i].g, enemies[i].b)
            if not (enemies[i].x + x_c < 0 or enemies[i].x + x_c > Dimensions.WIDTH or enemies[i].y + y_c < 0 or enemies[i].y + y_c > Dimensions.HEIGHT):
                enemies[i] = Enemy(background, enemies[i].x + x_c, enemies[i].y + y_c, enemies[i].r, enemies[i].g,
                                   enemies[i].b)
                i += 1

        pygame.display.update()
        clock.tick(75)


def find_shortest_path(current_x, current_y, goal_x, goal_y, speed):
    smjerovi = [(-speed, speed), (-speed, -speed), (speed, speed), (speed, -speed)]
    #lista = []
    dmin = inf
    x_final = 0
    y_final = 0
    for i in range(len(smjerovi)):
        x = smjerovi[i][0] + current_x
        y = smjerovi[i][1] + current_y
        #lista.append((floor(x), floor(y)))
        d = sqrt((x - goal_x) ** 2 + (y - goal_y) ** 2)
        if d < dmin:
            dmin = d
            x_final = x
            y_final = y
    return floor(x_final), floor(y_final)


if __name__ == '__main__':
    game_loop()
