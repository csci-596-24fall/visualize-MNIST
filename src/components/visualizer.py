
# Function to display the content on the right section
import pygame
from utils.colors import BLUE, GRAY, WHITE
from utils.constant import NN_SIZE, SCREEN_DIVIDER, SCREEN_HEIGHT, SCREEN_WIDTH

class Visualizer:
    LINE_COLOR = GRAY
    CELL_SIZE = 10

    def __init__(self, screen, font) -> None:
        self.screen = screen
        self.font = font 
    
    def update(self, layers):
        pygame.draw.rect(self.screen, WHITE, (
            SCREEN_DIVIDER,
            0,
            SCREEN_WIDTH - SCREEN_DIVIDER,
            SCREEN_HEIGHT))

        # TODO display some instruction here
        text = self.font.render("Display Area", True, BLUE)
        self.screen.blit(text, (SCREEN_DIVIDER + 20, 20))

        self._draw_matrix(NN_SIZE.INPUT, (SCREEN_DIVIDER + 10, 100), layers[0])
        self._draw_matrix(NN_SIZE.LAYER1, (SCREEN_DIVIDER + 300, 100), layers[1])
        self._draw_matrix(NN_SIZE.LAYER2, (SCREEN_DIVIDER + 480, 100), layers[2])
        self._draw_matrix(NN_SIZE.LAYER3, (SCREEN_DIVIDER + 550, 100), layers[3])


    def _draw_matrix(self, shape, offset, activation):
        height, width = shape
        offset_x, offset_y = offset

        print(activation.shape)
        print(shape)
        assert activation.shape == shape 

        # Draw activation
        for i in range(height):
            for j in range(width):
                # Get the value from the array
                value = activation[i][j]
                # Map value to 0-255 grayscale
                grey_shade = int((1 - value) * 255)
                if grey_shade < 0: grey_shade = 0
                if grey_shade > 255: grey_shade = 255
                color = (grey_shade, grey_shade, grey_shade)
                pygame.draw.rect(self.screen, color, 
                                (offset_x + j * self.CELL_SIZE, 
                                offset_y + i * self.CELL_SIZE, 
                                self.CELL_SIZE, self.CELL_SIZE))

        # Draw the grid
        for row in range(height + 1):
            pygame.draw.line(self.screen, self.LINE_COLOR, 
                            (offset_x,
                                offset_y + row * self.CELL_SIZE), 
                            (offset_x + width * self.CELL_SIZE,
                                 offset_y + row * self.CELL_SIZE),
                            1)

        for col in range(width + 1):
            pygame.draw.line(self.screen, self.LINE_COLOR, 
                            (offset_x + col * self.CELL_SIZE,
                                offset_y), 
                            (offset_x + col * self.CELL_SIZE,
                                offset_y + height * self.CELL_SIZE),
                            1)

        