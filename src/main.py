import pygame

from components.board import Board
from components.nn import visualize_nn
from utils.colors import BLACK
from utils.constant import *

def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR)
    pygame.display.set_caption(SCREEN_TITLE)
    font = pygame.font.Font(None, 36)

    # Init drawing board
    board = Board(screen)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            board.handle_event(event)

        # Update board
        # if event.pos[0] < SCREEN_DIVIDER:  # Ensure drawing only in the left section
        board.handle_iteration()

        # Draw the divider line
        pygame.draw.line(screen, BLACK, (SCREEN_DIVIDER, 0), (SCREEN_DIVIDER, SCREEN_HEIGHT), 2)
        # Display content on the right section

        visualize_nn(screen, font)
        # Update the display
        pygame.display.update()
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()