import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Color definitions
RED = (200, 0, 0)
BLUE = (0, 100, 255)
GREY = (230, 230, 230)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Game dimensions and settings
WIN_WIDTH = 600
WIN_HEIGHT = 400
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Initialize window
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Classic Snake Game")
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

def show_score(score):
    value = score_font.render(f"Score: {score}", True, BLACK)
    window.blit(value, [10, 10])

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(window, GREEN, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

def display_message(msg, color):
    message = font_style.render(msg, True, color)
    window.blit(message, [WIN_WIDTH / 6, WIN_HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    x = WIN_WIDTH / 2
    y = WIN_HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, WIN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(GREY)
            display_message("You Lost! Press P to Play Again or Q to Quit", RED)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Check for boundaries
        if x >= WIN_WIDTH or x < 0 or y >= WIN_HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change

        window.fill(GREY)
        pygame.draw.rect(window, YELLOW, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(snake_length - 1)
        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, WIN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Start game
game_loop()
# This is a simple implementation of the classic Snake game using Pygame.