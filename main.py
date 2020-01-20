import pygame
from random import randint, choice
from Snake import Snake
from Snake import Fruit
from Snake import Colors
from Snake import Dimensions
from Snake import Enemy
from math import inf, floor, sqrt
import time


def game_loop():
    pygame.init()
    background = pygame.display.set_mode((Dimensions.WIDTH, Dimensions.HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    snake = Snake(background, 100, Dimensions.TILE_SIZE)
    fruit = Fruit(background, randint(20, Dimensions.WIDTH - 20), randint(20, Dimensions.HEIGHT - 20))
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
    font = pygame.font.Font(None, 30)
    score_text = font.render('Score: ' + str(score), 2, Colors.YELLOW)
    box_width = score_text.get_rect()
    score_x = (Dimensions.WIDTH - box_width[2]) / 2
    background.blit(score_text, [score_x, 20])
    enemies = []

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and can_left:
                    x_change = -1 * speed
                    y_change = 0
                    can_left = False
                    can_right = False
                    can_up = True
                    can_down = True

                if event.key == pygame.K_RIGHT and can_right:
                    x_change = speed
                    y_change = 0
                    can_left = False
                    can_right = False
                    can_up = True
                    can_down = True

                if event.key == pygame.K_DOWN and can_down:
                    y_change = speed
                    x_change = 0
                    can_down = False
                    can_up = False
                    can_right = True
                    can_left = True

                if event.key == pygame.K_UP and can_up:
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
        background.blit(score_text, [score_x, 20])
        if Dimensions.d(snake.head_x, snake.head_y, fruit.x, fruit.y) < 4:
            fruit = Fruit(background, randint(20, Dimensions.WIDTH - 20), randint(20, Dimensions.HEIGHT - 20))
            score += 1
            score_text = font.render('Score: ' + str(score), 2, Colors.YELLOW)
            if score // 5 > 0 and score % 5 == 0:
                speed = 1.2 * speed
                enemies.append(
                    Enemy(background, randint(10, Dimensions.WIDTH - 10), randint(10, Dimensions.HEIGHT - 10),
                          randint(0, 255), randint(0, 255), randint(0, 255)))
        else:
            fruit = Fruit(background, fruit.x, fruit.y)
        i = 0
        while i < len(enemies):
            x_c = randint(-1, 1) * int(speed)
            y_c = randint(-1, 1) * int(speed)
            if not (enemies[i].x + x_c < 0 or enemies[i].x + x_c > Dimensions.WIDTH or enemies[i].y + y_c < 0 or
                    enemies[i].y + y_c > Dimensions.HEIGHT):
                enemies[i] = Enemy(background, enemies[i].x + x_c, enemies[i].y + y_c, enemies[i].r, enemies[i].g,
                                   enemies[i].b)
                detect_collision(enemies, x, y, background, score)
                i += 1

        pygame.display.update()
        clock.tick(75)


def detect_collision(enemies, current_x, current_y, background, score):
    for i in range(len(enemies)):
        if Dimensions.circle_square_collision(current_x, current_y, enemies[i].x, enemies[i].y):
            message_display(background, "GAME OVER!".format(score), 2, True)


def text_objects(text, font):
    text_surface = font.render(text, True, Colors.WHITE)
    return text_surface, text_surface.get_rect()


def message_display(game_display, text, sleep_time, game_over):
    large_text = pygame.font.Font("freesansbold.ttf", 70)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (Dimensions.WIDTH / 2, Dimensions.HEIGHT / 2)
    game_display.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(sleep_time)
    if game_over:
        game_loop()


def find_shortest_path(current_x, current_y, goal_x, goal_y, speed):
    axes = [(-speed, speed), (-speed, -speed), (speed, speed), (speed, -speed)]
    dmin = inf
    x_final = 0
    y_final = 0
    for i in range(len(axes)):
        x = axes[i][0] + current_x
        y = axes[i][1] + current_y
        d = sqrt((x - goal_x) ** 2 + (y - goal_y) ** 2)
        if d < dmin:
            dmin = d
            x_final = x
            y_final = y
    return floor(x_final), floor(y_final)


if __name__ == '__main__':
    game_loop()
