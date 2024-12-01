
# Function to display the content on the right section
import numpy as np
import pygame
from utils.colors import BLACK, GRAY, WHITE
from utils.constant import NN_SIZE, SCREEN_DIVIDER, SCREEN_HEIGHT, SCREEN_WIDTH
from utils.utils import normalize

class Visualizer:
    LINE_COLOR = GRAY
    CELL_SIZE = 10
    GAP = 10

    INPUT_LAYER_OFFSET_X = SCREEN_DIVIDER + GAP
    LAYER1_OFFSET_X = INPUT_LAYER_OFFSET_X + NN_SIZE.INPUT[1] * CELL_SIZE + GAP
    LAYER2_OFFSET_X = LAYER1_OFFSET_X + NN_SIZE.LAYER1[1] * CELL_SIZE + GAP
    LAYER3_OFFSET_X = LAYER2_OFFSET_X + NN_SIZE.LAYER2[1] * CELL_SIZE + GAP
    RESULT_OFFSET_X = LAYER3_OFFSET_X + GAP * 2

    LAYERS_OFFSET_Y = 30

    INPUT_LAYER_OFFSET = (INPUT_LAYER_OFFSET_X, LAYERS_OFFSET_Y)
    LAYER1_OFFSET = (LAYER1_OFFSET_X, LAYERS_OFFSET_Y)
    LAYER2_OFFSET = (LAYER2_OFFSET_X, LAYERS_OFFSET_Y)
    LAYER3_OFFSET = (LAYER3_OFFSET_X, LAYERS_OFFSET_Y)

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
            self.screen.blit(text_result, (self.RESULT_OFFSET_X, self.LAYERS_OFFSET_Y + result * self.CELL_SIZE))

        self._draw_grid(NN_SIZE.INPUT, self.INPUT_LAYER_OFFSET)
        self._draw_grid(NN_SIZE.LAYER1, self.LAYER1_OFFSET)
        self._draw_grid(NN_SIZE.LAYER2, self.LAYER2_OFFSET)
        self._draw_grid(NN_SIZE.LAYER3, self.LAYER3_OFFSET)

        # Draw instruction text
        text_instruction = self.font.render("press space to reset", True, BLACK)
        self.screen.blit(text_instruction, (SCREEN_DIVIDER + self.GAP, 350))

        # Draw input layer text
        text_input = self.font.render("Input", True, BLACK)
        self.screen.blit(text_input, (self.INPUT_LAYER_OFFSET_X, 10))

        # Draw layer1 text
        text_layer1 = self.font.render("Layer 1", True, BLACK)
        self.screen.blit(text_layer1, (self.LAYER1_OFFSET_X, 10))

        # Draw layer2 text
        text_layer2 = self.font.render("Layer 2", True, BLACK)
        self.screen.blit(text_layer2, (self.LAYER2_OFFSET_X, 10))

        # Draw layer3 text
        text_layer3 = self.font.render("Layer 3", True, BLACK)
        self.screen.blit(text_layer3, (self.LAYER3_OFFSET_X, 10))
    

    

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

        normalized = normalize(activation)

        # Draw activation
        for i in range(height):
            for j in range(width):
                # Get the value from the array
                value = normalized[i][j]

                # Map value to 0-255 grayscale
                grey_shade = int((1 - value) * 255)

                color = (grey_shade, grey_shade, grey_shade)
                pygame.draw.rect(self.screen, color, 
                                (offset_x + j * self.CELL_SIZE, 
                                offset_y + i * self.CELL_SIZE, 
                                self.CELL_SIZE, self.CELL_SIZE))
