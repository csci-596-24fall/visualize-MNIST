import pygame
import pygame.camera

from components.board import Board
from components.neural_network import NeuralNetwork
from components.visualizer import Visualizer
from utils.constant import SCREEN_COLOR, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

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
    # Init neural network
    nn = NeuralNetwork()
    # Init visualizer
    visualizer = Visualizer(screen, font)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            board.handle_event(event)

        # Update board
        board.handle_iteration()
        if board.is_updated():
            # Update Neural Network
            nn.update(board.get_img())
            # Update visualizer with drawing
            visualizer.update(nn.get_activations())

        # Update the display
        pygame.display.update()
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()