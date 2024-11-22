import pygame
import pygame.camera
import matplotlib.pyplot as plt # plotting library

from components.board import Board
from components.neural_network import NeuralNetwork
from components.visualizer import Visualizer
from utils.constant import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

def reset(board, visualizer):
    board.reset()
    visualizer.reset()


def main():
    # Init essential objects for pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)
    font = pygame.font.Font(pygame.font.get_default_font(), 12)

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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                reset(board, visualizer)
            # Press D to debug
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                plt.imshow(board.get_img(), cmap = 'gray')
                plt.show()
            board.handle_event(event)

        # Update board
        board.handle_iteration()
        # If board is updated, update neural network and visualizer
        if board.is_updated():
            # Update Neural Network
            nn.update(board.get_img())
            # Update visualizer with drawing
            visualizer.update(nn.get_layers())

        # Update the display
        pygame.display.update()
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()