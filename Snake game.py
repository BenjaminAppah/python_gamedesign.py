import pygame
import sys
import random
from pygame import mixer


# Initialize Pygame
pygame.init()
 
 # Background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Screen settings
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
icon = pygame.image.load('Snake.jpg')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BROWN = (25,5,6)


# Font
font = pygame.font.Font(None, 36)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake settings
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = RIGHT
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE, random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

def draw_snake(screen, snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0] * CELL_SIZE, head_y + direction[1] * CELL_SIZE)
    return [new_head] + snake[:-1]

def check_collision(snake):
    head = snake[0]
    return (head in snake[1:] or
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT)

def grow_snake(snake):
    snake.append(snake[-1])

def main():
    global direction, food

    clock = pygame.time.Clock()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        snake.insert(0, (snake[0][0] + direction[0] * CELL_SIZE, snake[0][1] + direction[1] * CELL_SIZE))
        if snake[0] == food:
            explosiòn_sound = mixer.Sound('Eating.mp3')
            explosiòn_sound.play()
            food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE, random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
            score += 1
        else:
            snake.pop()

        if check_collision(snake):
            pygame.quit()
            sys.exit()
       

        screen.fill(BROWN)
        draw_snake(screen, snake)
        draw_food(screen, food)

        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)
        pygame.display.update()
if __name__ == '__main__':
    main()