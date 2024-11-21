import pygame
import pygame.camera

from components.board import Board
from components.neural_network import NeuralNetwork
from components.visualizer import Visualizer
from utils.constant import SCREEN_COLOR, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

def reset(board, visualizer):
    board.reset()
    visualizer.reset()


def main():
    # Init essential objects for pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)
    font = pygame.font.Font(None, 24)

    # Init drawing board
    board = Board(screen)
    # Init neural network
    nn = NeuralNetwork()
    # Init visualizer
    visualizer = Visualizer(screen, font)

    reset(board, visualizer)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                reset(board, visualizer)

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