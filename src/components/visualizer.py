
# Function to display the content on the right section
import numpy as np
import pygame
from utils.colors import BLACK, GRAY, WHITE
from utils.constant import NN_SIZE, SCREEN_DIVIDER, SCREEN_HEIGHT, SCREEN_WIDTH

class Visualizer:
    LINE_COLOR = GRAY
    CELL_SIZE = 10

    INPUT_LAYER_OFFSET = (SCREEN_DIVIDER + 10, 100)
    LAYER1_OFFSET = (SCREEN_DIVIDER + 300, 100)
    LAYER2_OFFSET = (SCREEN_DIVIDER + 470, 100)
    LAYER3_OFFSET = (SCREEN_DIVIDER + 520, 100)
    RESULT_OFFSET_X = SCREEN_DIVIDER + 540

    def __init__(self, screen, font) -> None:
        self.screen = screen
        self.font = font 
    
    def update(self, layers = None):
        # Draw background
        pygame.draw.rect(self.screen, WHITE, (
            SCREEN_DIVIDER,
            0,
            SCREEN_WIDTH - SCREEN_DIVIDER,
            SCREEN_HEIGHT))

        if layers:
            self._draw_activation(NN_SIZE.INPUT, self.INPUT_LAYER_OFFSET, layers[0])
            self._draw_activation(NN_SIZE.LAYER1, self.LAYER1_OFFSET, layers[1])
            self._draw_activation(NN_SIZE.LAYER2, self.LAYER2_OFFSET, layers[2])
            self._draw_activation(NN_SIZE.LAYER3, self.LAYER3_OFFSET, layers[3])

            result = np.argmax(layers[3])
            text_result = self.font.render(f"{result}", True, BLACK)
            self.screen.blit(text_result, (self.RESULT_OFFSET_X, 100 + result * self.CELL_SIZE))

        self._draw_grid(NN_SIZE.INPUT, self.INPUT_LAYER_OFFSET)
        self._draw_grid(NN_SIZE.LAYER1, self.LAYER1_OFFSET)
        self._draw_grid(NN_SIZE.LAYER2, self.LAYER2_OFFSET)
        self._draw_grid(NN_SIZE.LAYER3, self.LAYER3_OFFSET)

        # Draw instruction text
        text_instruction = self.font.render("press any key to reset", True, BLACK)
        self.screen.blit(text_instruction, (SCREEN_DIVIDER + 20, 20))
    
    def reset(self):
        self.update()
    

    def _draw_grid(self, shape, offset):
        height, width = shape
        offset_x, offset_y = offset

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

    def _draw_activation(self, shape, offset, activation):
        height, width = shape
        offset_x, offset_y = offset

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
