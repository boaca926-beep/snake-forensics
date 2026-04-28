import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants; game basic attributions
CELL_SIZE = 30  # Size of a single cell
GRID_WIDTH = 30  # Number of grids to width
GRID_HEIGHT = 30  # Number of grids to HEIGHT
WIDTH = GRID_WIDTH * CELL_SIZE  # Total width
HEIGHT = GRID_HEIGHT * CELL_SIZE  # Total HEIGHT
FPS = 5  # Game speed moves per second

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 150, 0)
GRAY = (50, 50, 50)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def draw_grid(screen):
    """
    Draw grid lines for better visibility.
    """

    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def draw_tank(screen, tank):
    """"""
    for segment in tank:
        body = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, body)  # body
        pygame.draw.rect(screen, DARK_GREEN, body, 2)  # body border


def reset_game():
    """"""
    # Initial tank
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2 + 12
    tank = [
        (start_x, start_y),
        (start_x - 1, start_y),
        (start_x - 2, start_y),
        (start_x - 1, start_y - 1),
    ]

    return tank


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # Game state
    game_over = False
    tank = reset_game()
    print(tank)

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Here we quit!")
                running = False
                pygame.quit()
                sys.exit()

        if not game_over:
            # Update Game Logic
            print("Game is runnning ...")

        # Drawing
        screen.fill(BLACK)
        draw_grid(screen)
        draw_tank(screen, tank)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    print("Starting my game ...")
    main()
