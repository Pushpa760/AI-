import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
ROWS = 20
CELL_SIZE = WIDTH // ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Color Changing Snake Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake_colors = [
    (0, 200, 0),      # Green
    (255, 0, 0),      # Red
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 0, 255),    # Pink
    (0, 255, 255),    # Cyan
    (255, 165, 0)     # Orange
]

emoji_font = pygame.font.SysFont("Segoe UI Emoji", 24)
font = pygame.font.SysFont("Arial", 30)


def generate_foods():
    foods = []

    while len(foods) < 4:
        pos = (
            random.randint(0, ROWS - 1),
            random.randint(0, ROWS - 1)
        )

        if pos not in foods:
            foods.append(pos)

    return foods


def reset_game():

    global current_color

    snake_pos = [5, 5]
    direction = [1, 0]

    foods = generate_foods()

    score = 0

    current_color = snake_colors[0]

    return snake_pos, direction, foods, score


snake_pos, direction, foods, score = reset_game()

game_over = False
running = True

while running:

    clock.tick(7)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if not game_over:

                if event.key == pygame.K_UP and direction != [0, 1]:
                    direction = [0, -1]

                elif event.key == pygame.K_DOWN and direction != [0, -1]:
                    direction = [0, 1]

                elif event.key == pygame.K_LEFT and direction != [1, 0]:
                    direction = [-1, 0]

                elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
                    direction = [1, 0]

            if game_over and event.key == pygame.K_r:
                snake_pos, direction, foods, score = reset_game()
                game_over = False

    if not game_over:

        snake_pos[0] += direction[0]
        snake_pos[1] += direction[1]

        if (
            snake_pos[0] < 0 or
            snake_pos[0] >= ROWS or
            snake_pos[1] < 0 or
            snake_pos[1] >= ROWS
        ):
            game_over = True

        current_pos = (snake_pos[0], snake_pos[1])

        if current_pos in foods:

            score += 1

            current_color = random.choice(snake_colors)

            foods.remove(current_pos)

            while len(foods) < 4:

                pos = (
                    random.randint(0, ROWS - 1),
                    random.randint(0, ROWS - 1)
                )

                if pos not in foods:
                    foods.append(pos)

    screen.fill(BLACK)

    # Snake Color Changing Background
    pygame.draw.rect(
        screen,
        current_color,
        (
            snake_pos[0] * CELL_SIZE,
            snake_pos[1] * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
    )

    # Snake Emoji
    snake_emoji = emoji_font.render("🐍", True, WHITE)

    screen.blit(
        snake_emoji,
        (
            snake_pos[0] * CELL_SIZE,
            snake_pos[1] * CELL_SIZE
        )
    )

    # Fruits
    for food in foods:

        apple = emoji_font.render("🍎", True, RED)

        screen.blit(
            apple,
            (
                food[0] * CELL_SIZE,
                food[1] * CELL_SIZE
            )
        )

    # Score
    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    # Game Over Screen
    if game_over:

        over_text = font.render(
            "Game Over! Press R to Restart",
            True,
            RED
        )

        screen.blit(
            over_text,
            (40, HEIGHT // 2)
        )

    pygame.display.update()

pygame.quit()