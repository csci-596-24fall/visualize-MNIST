
# Function to display the content on the right section
import pygame
from utils.colors import BLUE, GRAY
from utils.constant import SCREEN_DIVIDER, SCREEN_HEIGHT, SCREEN_WIDTH


def visualize_nn(screen, font):
    pygame.draw.rect(screen, GRAY, (SCREEN_DIVIDER,
                                    0, SCREEN_WIDTH - SCREEN_DIVIDER, SCREEN_HEIGHT))
    text = font.render("Right Section: Display Area", True, BLUE)
    screen.blit(text, (SCREEN_DIVIDER + 20, 20))
